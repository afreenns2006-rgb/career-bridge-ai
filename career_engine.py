"""
Career recommendation engine for Career Bridge AI.

Provides career recommendations based on user skills, experience,
education, and preferences.
"""

from typing import Any, Optional
import logging
import pandas as pd
from pathlib import Path

from database import get_db_manager
from config import CAREERS_CSV

logger = logging.getLogger(__name__)

CAREER_FALLBACKS = {
    "data": {
        "career_name": "Data Analyst",
        "required_skills": ["Python", "SQL", "Excel", "Data Visualization", "Statistics"],
        "learning_roadmap": ["Learn SQL basics", "Practice Pandas", "Build dashboards", "Create a data portfolio"],
    },
    "machine": {
        "career_name": "AI/ML Beginner",
        "required_skills": ["Python", "Machine Learning", "Statistics", "Data Analysis", "Model Evaluation"],
        "learning_roadmap": ["Revise Python", "Study ML basics", "Build beginner ML projects", "Deploy one simple model"],
    },
    "web": {
        "career_name": "Web Developer",
        "required_skills": ["HTML", "CSS", "JavaScript", "React", "APIs"],
        "learning_roadmap": ["Build HTML/CSS layouts", "Learn JavaScript", "Create React projects", "Deploy a portfolio website"],
    },
    "programming": {
        "career_name": "Software Developer",
        "required_skills": ["Programming", "Java", "C", "Python", "Git", "Data Structures"],
        "learning_roadmap": ["Strengthen programming basics", "Practice DSA", "Build projects", "Publish code on GitHub"],
    },
    "cloud": {
        "career_name": "Cloud Engineer",
        "required_skills": ["Linux", "Cloud Computing", "AWS", "Docker", "Networking"],
        "learning_roadmap": ["Learn Linux", "Study cloud basics", "Practice Docker", "Deploy an app on cloud"],
    },
    "security": {
        "career_name": "Cybersecurity Analyst",
        "required_skills": ["Linux", "Networking", "Security Basics", "Python", "Incident Response"],
        "learning_roadmap": ["Learn networking", "Practice Linux", "Study OWASP", "Document security labs"],
    },
    "default": {
        "career_name": "Software Developer",
        "required_skills": ["Python", "Problem Solving", "Git", "Data Structures", "APIs"],
        "learning_roadmap": ["Strengthen programming basics", "Practice DSA", "Build projects", "Publish code on GitHub"],
    },
}

# Default careers database
DEFAULT_CAREERS = [
    {
        "career": "Software Developer",
        "required_skills": "python,java,javascript",
        "min_experience": 0,
        "salary_range": "60000-120000",
        "growth": "High",
    },
    {
        "career": "Data Scientist",
        "required_skills": "python,machine learning,statistics,sql",
        "min_experience": 1,
        "salary_range": "80000-150000",
        "growth": "Very High",
    },
    {
        "career": "DevOps Engineer",
        "required_skills": "docker,kubernetes,aws,git",
        "min_experience": 2,
        "salary_range": "90000-160000",
        "growth": "High",
    },
    {
        "career": "Full Stack Developer",
        "required_skills": "javascript,react,node.js,sql,html,css",
        "min_experience": 1,
        "salary_range": "70000-140000",
        "growth": "High",
    },
    {
        "career": "Cloud Architect",
        "required_skills": "aws,azure,gcp,kubernetes",
        "min_experience": 3,
        "salary_range": "120000-200000",
        "growth": "High",
    },
    {
        "career": "ML Engineer",
        "required_skills": "python,machine learning,deep learning,tensorflow",
        "min_experience": 2,
        "salary_range": "100000-180000",
        "growth": "Very High",
    },
    {
        "career": "Database Administrator",
        "required_skills": "sql,mongodb,postgresql,oracle",
        "min_experience": 2,
        "salary_range": "80000-140000",
        "growth": "Medium",
    },
    {
        "career": "Solutions Architect",
        "required_skills": "design,leadership,communication,technical knowledge",
        "min_experience": 3,
        "salary_range": "110000-170000",
        "growth": "High",
    },
]


class CareerRecommendationEngine:
    """
    Generates career recommendations based on user profile.

    Analyzes skills, education, experience, and preferences to suggest
    suitable career paths with skill gap analysis.
    """

    def __init__(self) -> None:
        """
        Initialize career recommendation engine.

        TODO: Implement engine initialization and load models.
        """
        self.careers_df: Optional[pd.DataFrame] = None
        try:
            self.db_manager = get_db_manager()
        except Exception as exc:
            logger.warning("Database unavailable for career engine; continuing with in-memory data: %s", exc)
            self.db_manager = None
        self.load_careers()

    def load_careers(self) -> pd.DataFrame:
        """
        Load careers database from CSV.

        Returns:
            DataFrame with careers and required skills.

        TODO: Implement career data loading from CAREERS_CSV.
        """
        try:
            if CAREERS_CSV.exists():
                self.careers_df = pd.read_csv(CAREERS_CSV)
            else:
                self.careers_df = pd.DataFrame(DEFAULT_CAREERS)
        except Exception as e:
            logger.warning(f"Could not load careers CSV: {e}. Using defaults.")
            self.careers_df = pd.DataFrame(DEFAULT_CAREERS)

        return self.careers_df

    def recommend_careers(
        self,
        user_skills: list[str],
        education: str,
        experience_years: int,
        preferences: Optional[dict[str, Any]] = None,
    ) -> list[dict[str, Any]]:
        """
        Generate career recommendations for user.

        Args:
            user_skills: List of user's current skills.
            education: User's educational background.
            experience_years: Years of professional experience.
            preferences: Optional user preferences (industry, salary, etc).

        Returns:
            List of career recommendations with match scores and details.

        TODO: Implement recommendation algorithm using:
            - Skill matching
            - Experience alignment
            - Education requirements
            - User preferences
        """
        if self.careers_df is None:
            self.load_careers()

        recommendations = []
        user_skills = [skill for skill in user_skills if skill]
        user_skills_lower = [s.lower() for s in user_skills]
        preferences = preferences or {}
        career_column = self._resolve_column("career", "career_name", "title", "role")
        skills_column = self._resolve_column("required_skills", "skills", "skill")
        min_experience_column = self._resolve_column("min_experience", "experience", "experience_years")
        salary_column = self._resolve_column("salary_range", "salary", "salary_estimate")
        growth_column = self._resolve_column("growth", "growth_potential", "demand")
        description_column = self._resolve_column("description", "summary")

        if not career_column or not skills_column:
            logger.warning("Career data is missing required columns. Using fallback recommendation.")
            return self.generate_fallback_recommendations(user_skills, education, experience_years, preferences)

        for _, career_row in self.careers_df.iterrows():
            career_name = str(career_row.get(career_column, "")).strip()
            if not career_name or career_name.lower() == "unknown":
                continue
            required_skills_str = str(career_row.get(skills_column, ""))
            required_skills = [s.strip() for s in required_skills_str.split(",") if s.strip()]
            min_experience = self._safe_int(career_row.get(min_experience_column, 0) if min_experience_column else 0)

            # Calculate skill match score
            matching_skills = len([s for s in required_skills if s.lower() in user_skills_lower])
            skill_match = (matching_skills / len(required_skills) * 100) if required_skills else 0

            # Experience score
            experience_score = (
                100 if experience_years >= min_experience else (experience_years / max(min_experience, 1) * 80)
            )

            # Overall match score
            overall_score = skill_match * 0.6 + experience_score * 0.4

            if overall_score > 30:  # Only show careers with at least 30% match
                recommendations.append(
                    {
                        "career_name": career_name,
                        "match_score": round(overall_score, 1),
                        "skill_match": round(skill_match, 1),
                        "required_skills": required_skills,
                        "matching_skills": [s for s in required_skills if s.lower() in user_skills_lower],
                        "missing_skills": [s for s in required_skills if s.lower() not in user_skills_lower],
                        "salary_range": career_row.get(salary_column, "Not specified") if salary_column else "Not specified",
                        "growth_potential": career_row.get(growth_column, "Growing") if growth_column else "Growing",
                        "description": career_row.get(description_column, "") if description_column else "",
                        "learning_roadmap": self._build_learning_roadmap(required_skills, user_skills_lower),
                        "suggested_next_steps": self._build_next_steps(required_skills, user_skills_lower),
                        "source": "career_data",
                    }
                )

        ranked = self.rank_recommendations(recommendations)
        if ranked:
            return ranked

        return self.generate_fallback_recommendations(user_skills, education, experience_years, preferences)

    def _resolve_column(self, *candidates: str) -> Optional[str]:
        """Return the first available dataframe column from candidate names."""
        if self.careers_df is None:
            self.load_careers()
        columns = set(self.careers_df.columns)
        logger.info("Available career dataframe columns: %s", list(self.careers_df.columns))
        for column in candidates:
            if column in columns:
                return column
        return None

    @staticmethod
    def _safe_int(value: Any) -> int:
        """Convert values from CSV to int safely."""
        try:
            if pd.isna(value):
                return 0
            return int(float(value))
        except (TypeError, ValueError):
            return 0

    @staticmethod
    def _build_learning_roadmap(required_skills: list[str], user_skills_lower: list[str]) -> list[str]:
        """Build a short learning roadmap from missing skills."""
        missing = [skill for skill in required_skills if skill.lower() not in user_skills_lower]
        focus_skills = missing[:4] or required_skills[:4]
        return [
            f"Learn or revise {skill}" for skill in focus_skills
        ] + ["Build one portfolio project", "Update your resume with measurable outcomes"]

    @staticmethod
    def _build_next_steps(required_skills: list[str], user_skills_lower: list[str]) -> list[str]:
        """Build practical next steps for the recommendation."""
        missing = [skill for skill in required_skills if skill.lower() not in user_skills_lower]
        next_steps = [
            "Choose one target role and study 2-3 matching job descriptions.",
            "Add relevant projects and achievements to your resume.",
        ]
        if missing:
            next_steps.insert(0, f"Start with this skill gap: {', '.join(missing[:3])}.")
        else:
            next_steps.insert(0, "You already match the core skills. Focus on projects and interview practice.")
        return next_steps

    def generate_fallback_recommendations(
        self,
        user_skills: list[str],
        education: str,
        experience_years: int,
        preferences: Optional[dict[str, Any]] = None,
    ) -> list[dict[str, Any]]:
        """Generate meaningful career suggestions when data or model matching fails."""
        preferences = preferences or {}
        search_text = " ".join(
            user_skills
            + [
                education,
                str(preferences.get("domain", "")),
                str(preferences.get("interests", "")),
                str(preferences.get("goals", "")),
            ]
        ).lower()

        search_tokens = {token.strip(" /,.;:()[]{}") for token in search_text.split()}

        if any(word in search_text for word in ["data", "sql", "excel", "analytics", "pandas"]):
            fallback = CAREER_FALLBACKS["data"]
        elif any(word in search_text for word in ["web", "react", "html", "css", "javascript"]):
            fallback = CAREER_FALLBACKS["web"]
        elif any(word in search_text for word in ["java", "programming", "software", "developer", "coding"]) or "c" in search_tokens:
            fallback = CAREER_FALLBACKS["programming"]
        elif any(word in search_text for word in ["machine", "ml", "ai", "tensorflow", "pytorch", "tech", "technology"]):
            fallback = CAREER_FALLBACKS["machine"]
        elif any(word in search_text for word in ["cloud", "aws", "azure", "docker"]):
            fallback = CAREER_FALLBACKS["cloud"]
        elif any(word in search_text for word in ["security", "cyber", "network"]):
            fallback = CAREER_FALLBACKS["security"]
        else:
            fallback = CAREER_FALLBACKS["machine"]

        user_skills_lower = [skill.lower() for skill in user_skills]
        required_skills = fallback["required_skills"]
        matching_skills = [skill for skill in required_skills if skill.lower() in user_skills_lower]
        missing_skills = [skill for skill in required_skills if skill.lower() not in user_skills_lower]
        skill_match = (len(matching_skills) / len(required_skills) * 100) if required_skills else 0
        experience_bonus = min(max(experience_years, 0) * 5, 20)

        return [
            {
                "career_name": fallback["career_name"],
                "match_score": round(max(55, min(skill_match + 35 + experience_bonus, 95)), 1),
                "skill_match": round(skill_match, 1),
                "required_skills": required_skills,
                "matching_skills": matching_skills,
                "missing_skills": missing_skills,
                "salary_range": "Varies by location and experience",
                "growth_potential": "Promising",
                "description": "Rule-based fallback recommendation created from your profile.",
                "learning_roadmap": fallback["learning_roadmap"],
                "suggested_next_steps": self._build_next_steps(required_skills, user_skills_lower),
                "source": "fallback",
            }
        ]

    def calculate_skill_gap(self, current_skills: list[str], target_career: str) -> dict[str, Any]:
        """
        Calculate skill gap for target career.

        Args:
            current_skills: List of user's current skills.
            target_career: Target career path.

        Returns:
            Dictionary with missing skills and learning priorities.

        TODO: Implement skill gap analysis.
        """
        career_details = self.get_career_details(target_career)
        if not career_details:
            return {"error": f"Career '{target_career}' not found"}

        current_skills_lower = [s.lower() for s in current_skills]
        required_skills = career_details.get("required_skills", [])

        missing_skills = [s for s in required_skills if s.lower() not in current_skills_lower]

        return {
            "target_career": target_career,
            "current_skills_count": len(current_skills),
            "required_skills_count": len(required_skills),
            "matching_skills": [s for s in required_skills if s.lower() in current_skills_lower],
            "missing_skills": missing_skills,
            "learning_priority": len(missing_skills),
            "skill_gap_percentage": round(
                (len(missing_skills) / len(required_skills) * 100) if required_skills else 0, 1
            ),
        }

    def get_career_details(self, career_name: str) -> dict[str, Any]:
        """
        Get detailed information about a career.

        Args:
            career_name: Name of the career.

        Returns:
            Dictionary with career details, requirements, growth prospects.

        TODO: Implement career detail retrieval.
        """
        if self.careers_df is None:
            self.load_careers()

        career_column = self._resolve_column("career", "career_name", "title", "role")
        skills_column = self._resolve_column("required_skills", "skills", "skill")
        min_experience_column = self._resolve_column("min_experience", "experience", "experience_years")
        salary_column = self._resolve_column("salary_range", "salary", "salary_estimate")
        growth_column = self._resolve_column("growth", "growth_potential", "demand")

        if not career_column or not skills_column:
            logger.warning(
                "Career details unavailable. Required columns missing from dataframe: %s",
                list(self.careers_df.columns),
            )
            return {}

        career_series = self.careers_df[career_column].astype(str).str.lower()
        career_row = self.careers_df[career_series == career_name.lower()]
        if career_row.empty:
            return {}

        row = career_row.iloc[0]
        required_skills = [s.strip() for s in str(row.get(skills_column, "")).split(",") if s.strip()]

        return {
            "career_name": row.get(career_column, ""),
            "required_skills": required_skills,
            "min_experience": self._safe_int(row.get(min_experience_column, 0) if min_experience_column else 0),
            "salary_range": row.get(salary_column, "Not specified") if salary_column else "Not specified",
            "growth_potential": row.get(growth_column, "Promising") if growth_column else "Promising",
        }

    def get_similar_careers(self, career_name: str, count: int = 5) -> list[dict[str, Any]]:
        """
        Get similar career recommendations.

        Args:
            career_name: Reference career name.
            count: Number of similar careers to return.

        Returns:
            List of similar career recommendations.

        TODO: Implement similar career finding.
        """
        if self.careers_df is None:
            self.load_careers()

        career_details = self.get_career_details(career_name)
        if not career_details:
            return []

        career_column = self._resolve_column("career", "career_name", "title", "role")
        skills_column = self._resolve_column("required_skills", "skills", "skill")
        if not career_column or not skills_column:
            logger.warning(
                "Similar careers unavailable. Required columns missing from dataframe: %s",
                list(self.careers_df.columns),
            )
            return []

        reference_skills = {s.lower() for s in career_details.get("required_skills", [])}

        similar = []
        for _, career_row in self.careers_df.iterrows():
            current_career = str(career_row.get(career_column, "")).strip()
            if not current_career:
                continue
            if current_career.lower() == career_name.lower():
                continue

            current_skills = {
                s.strip().lower() for s in str(career_row.get(skills_column, "")).split(",") if s.strip()
            }

            # Calculate Jaccard similarity
            intersection = len(reference_skills & current_skills)
            union = len(reference_skills | current_skills)
            similarity = (intersection / union * 100) if union > 0 else 0

            if similarity > 20:
                similar.append(
                    {
                        "career_name": current_career,
                        "similarity_score": round(similarity, 1),
                        "common_skills": list(reference_skills & current_skills),
                    }
                )

        similar.sort(key=lambda x: x["similarity_score"], reverse=True)
        return similar[:count]

    def rank_recommendations(self, recommendations: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """
        Rank career recommendations by relevance.

        Args:
            recommendations: List of career recommendations.

        Returns:
            Ranked list of recommendations.

        TODO: Implement ranking algorithm.
        """
        return sorted(recommendations, key=lambda x: x.get("match_score", 0), reverse=True)
