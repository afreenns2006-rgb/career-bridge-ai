"""
Career recommendation engine for Career Bridge AI.

Provides career recommendations based on user skills, experience,
education, and preferences.
"""

from typing import List, Dict, Any, Optional
import logging
import pandas as pd
from pathlib import Path

from database import get_db_manager
from config import CAREERS_CSV

logger = logging.getLogger(__name__)

# Default careers database
DEFAULT_CAREERS = [
    {"career": "Software Developer", "required_skills": "python,java,javascript", "min_experience": 0, "salary_range": "60000-120000", "growth": "High"},
    {"career": "Data Scientist", "required_skills": "python,machine learning,statistics,sql", "min_experience": 1, "salary_range": "80000-150000", "growth": "Very High"},
    {"career": "DevOps Engineer", "required_skills": "docker,kubernetes,aws,git", "min_experience": 2, "salary_range": "90000-160000", "growth": "High"},
    {"career": "Full Stack Developer", "required_skills": "javascript,react,node.js,sql,html,css", "min_experience": 1, "salary_range": "70000-140000", "growth": "High"},
    {"career": "Cloud Architect", "required_skills": "aws,azure,gcp,kubernetes", "min_experience": 3, "salary_range": "120000-200000", "growth": "High"},
    {"career": "ML Engineer", "required_skills": "python,machine learning,deep learning,tensorflow", "min_experience": 2, "salary_range": "100000-180000", "growth": "Very High"},
    {"career": "Database Administrator", "required_skills": "sql,mongodb,postgresql,oracle", "min_experience": 2, "salary_range": "80000-140000", "growth": "Medium"},
    {"career": "Solutions Architect", "required_skills": "design,leadership,communication,technical knowledge", "min_experience": 3, "salary_range": "110000-170000", "growth": "High"}
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
        self.db_manager = get_db_manager()
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
        user_skills: List[str],
        education: str,
        experience_years: int,
        preferences: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
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
        user_skills_lower = [s.lower() for s in user_skills]
        
        for _, career_row in self.careers_df.iterrows():
            career_name = career_row.get("career", "Unknown")
            required_skills_str = career_row.get("required_skills", "")
            required_skills = [s.strip() for s in required_skills_str.split(",")]
            min_experience = int(career_row.get("min_experience", 0))
            
            # Calculate skill match score
            matching_skills = len([s for s in required_skills if s.lower() in user_skills_lower])
            skill_match = (matching_skills / len(required_skills) * 100) if required_skills else 0
            
            # Experience score
            experience_score = 100 if experience_years >= min_experience else (experience_years / max(min_experience, 1) * 80)
            
            # Overall match score
            overall_score = (skill_match * 0.6 + experience_score * 0.4)
            
            if overall_score > 30:  # Only show careers with at least 30% match
                recommendations.append({
                    "career_name": career_name,
                    "match_score": round(overall_score, 1),
                    "skill_match": round(skill_match, 1),
                    "required_skills": required_skills,
                    "matching_skills": [s for s in required_skills if s.lower() in user_skills_lower],
                    "missing_skills": [s for s in required_skills if s.lower() not in user_skills_lower],
                    "salary_range": career_row.get("salary_range", "Not specified"),
                    "growth_potential": career_row.get("growth", "Unknown")
                })
        
        return self.rank_recommendations(recommendations)
    
    def calculate_skill_gap(
        self,
        current_skills: List[str],
        target_career: str
    ) -> Dict[str, Any]:
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
            "skill_gap_percentage": round((len(missing_skills) / len(required_skills) * 100) if required_skills else 0, 1)
        }
    
    def get_career_details(self, career_name: str) -> Dict[str, Any]:
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
        
        career_row = self.careers_df[self.careers_df["career"].str.lower() == career_name.lower()]
        if career_row.empty:
            return {}
        
        row = career_row.iloc[0]
        required_skills = [s.strip() for s in str(row.get("required_skills", "")).split(",")]
        
        return {
            "career_name": row.get("career", ""),
            "required_skills": required_skills,
            "min_experience": int(row.get("min_experience", 0)),
            "salary_range": row.get("salary_range", "Not specified"),
            "growth_potential": row.get("growth", "Unknown")
        }
    
    def get_similar_careers(
        self,
        career_name: str,
        count: int = 5
    ) -> List[Dict[str, Any]]:
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
        
        reference_skills = set(s.lower() for s in career_details.get("required_skills", []))
        
        similar = []
        for _, career_row in self.careers_df.iterrows():
            current_career = career_row.get("career", "")
            if current_career.lower() == career_name.lower():
                continue
            
            current_skills = set(s.strip().lower() for s in str(career_row.get("required_skills", "")).split(","))
            
            # Calculate Jaccard similarity
            intersection = len(reference_skills & current_skills)
            union = len(reference_skills | current_skills)
            similarity = (intersection / union * 100) if union > 0 else 0
            
            if similarity > 20:
                similar.append({
                    "career_name": current_career,
                    "similarity_score": round(similarity, 1),
                    "common_skills": list(reference_skills & current_skills)
                })
        
        similar.sort(key=lambda x: x["similarity_score"], reverse=True)
        return similar[:count]
    
    def rank_recommendations(
        self,
        recommendations: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Rank career recommendations by relevance.
        
        Args:
            recommendations: List of career recommendations.
            
        Returns:
            Ranked list of recommendations.
            
        TODO: Implement ranking algorithm.
        """
        return sorted(recommendations, key=lambda x: x.get("match_score", 0), reverse=True)
