"""
Opportunity discovery engine for Career Bridge AI.

Provides relevant opportunities (internships, jobs, competitions)
based on user skills and preferences.
"""

from typing import List, Dict, Any, Optional
import logging
import pandas as pd
from datetime import datetime

from database import get_db_manager
from config import OPPORTUNITIES_CSV

logger = logging.getLogger(__name__)

# Default opportunities database
DEFAULT_OPPORTUNITIES = [
    {
        "name": "Google Summer Intern",
        "type": "internship",
        "skills": "python,algorithms",
        "stipend": 50000,
        "deadline": "2026-07-15",
        "category": "tech",
    },
    {
        "name": "Microsoft Internship",
        "type": "internship",
        "skills": "java,sql,cloud",
        "stipend": 45000,
        "deadline": "2026-08-01",
        "category": "tech",
    },
    {
        "name": "DataHack Competition",
        "type": "competition",
        "skills": "machine learning,python",
        "prize": 100000,
        "deadline": "2026-07-31",
        "category": "data",
    },
    {
        "name": "HackTheBox Challenge",
        "type": "competition",
        "skills": "cybersecurity,linux",
        "prize": 50000,
        "deadline": "2026-08-15",
        "category": "security",
    },
    {
        "name": "AI Bootcamp",
        "type": "bootcamp",
        "skills": "python,machine learning",
        "stipend": 25000,
        "deadline": "2026-06-30",
        "category": "learning",
    },
]


class OpportunityEngine:
    """
    Generates opportunity recommendations based on user profile.

    Discovers internships, job openings, competitions, and other
    career-building opportunities matching user skills.
    """

    def __init__(self) -> None:
        """
        Initialize opportunity discovery engine.

        TODO: Implement engine initialization.
        """
        self.opportunities_df: Optional[pd.DataFrame] = None
        self.db_manager = get_db_manager()
        self.load_opportunities()

    def load_opportunities(self) -> pd.DataFrame:
        """
        Load opportunities database from CSV.

        Returns:
            DataFrame with opportunities and requirements.

        TODO: Implement opportunity data loading from OPPORTUNITIES_CSV.
        """
        try:
            if OPPORTUNITIES_CSV.exists():
                self.opportunities_df = pd.read_csv(OPPORTUNITIES_CSV)
            else:
                self.opportunities_df = pd.DataFrame(DEFAULT_OPPORTUNITIES)
        except Exception as e:
            logger.warning(f"Could not load opportunities CSV: {e}. Using defaults.")
            self.opportunities_df = pd.DataFrame(DEFAULT_OPPORTUNITIES)

        logger.info("Available opportunity dataframe columns: %s", list(self.opportunities_df.columns))
        return self.opportunities_df

    def _resolve_column(self, *candidates: str) -> Optional[str]:
        """
        Return the first available dataframe column from the candidate names.
        """
        if self.opportunities_df is None:
            self.load_opportunities()

        columns = set(self.opportunities_df.columns)
        for column in candidates:
            if column in columns:
                return column

        logger.warning(
            "Missing expected opportunity column. Tried %s. Available columns: %s",
            candidates,
            list(self.opportunities_df.columns),
        )
        return None

    def recommend_opportunities(
        self,
        user_skills: list[str],
        education_level: str,
        experience_years: int,
        preferences: Optional[dict[str, Any]] = None,
    ) -> list[dict[str, Any]]:
        """
        Generate opportunity recommendations for user.

        Args:
            user_skills: List of user's current skills.
            education_level: User's education level.
            experience_years: Years of experience.
            preferences: Optional preferences (salary, location, etc).

        Returns:
            List of matching opportunities with match scores.

        TODO: Implement opportunity matching algorithm using:
            - Skill matching
            - Education requirements
            - Experience requirements
            - User preferences
            - Application deadlines
        """
        if self.opportunities_df is None:
            self.load_opportunities()

        recommendations = []
        user_skills_lower = [s.lower() for s in user_skills]
        name_column = self._resolve_column("name", "title", "opportunity_name")
        skills_column = self._resolve_column("skills", "skill", "required_skills")
        type_column = self._resolve_column("type", "category", "opportunity_type")
        category_column = self._resolve_column("category")
        stipend_column = self._resolve_column("stipend", "prize")
        deadline_column = self._resolve_column("deadline", "date")
        link_column = self._resolve_column("application_link", "link")

        if not name_column or not skills_column:
            return recommendations

        for _, opp_row in self.opportunities_df.iterrows():
            opp_name = opp_row.get(name_column, "")
            required_skills_str = opp_row.get(skills_column, "")
            required_skills = [s.strip() for s in str(required_skills_str).split(",")]

            # Calculate skill match
            matching_skills = len([s for s in required_skills if s.lower() in user_skills_lower])
            skill_match = (matching_skills / len(required_skills) * 100) if required_skills else 0

            # Include opportunities with at least 50% skill match
            if skill_match >= 50:
                recommendations.append(
                    {
                        "opportunity_name": opp_name,
                        "opportunity_type": opp_row.get(type_column, "") if type_column else "",
                        "category": opp_row.get(category_column, "") if category_column else "",
                        "match_score": round(skill_match, 1),
                        "required_skills": required_skills,
                        "matching_skills": [s for s in required_skills if s.lower() in user_skills_lower],
                        "stipend_or_prize": opp_row.get(stipend_column, 0) if stipend_column else 0,
                        "deadline": opp_row.get(deadline_column, "") if deadline_column else "",
                        "application_link": (
                            opp_row.get(link_column, "")
                            if link_column
                            else f"https://opportunities.example.com/{opp_name.replace(' ', '-').lower()}"
                        ),
                    }
                )

        return sorted(recommendations, key=lambda x: x.get("match_score", 0), reverse=True)

    def search_opportunities(self, query: str, filters: Optional[dict[str, Any]] = None) -> list[dict[str, Any]]:
        """
        Search opportunities by keyword and filters.

        Args:
            query: Search query string.
            filters: Optional filters (category, skills, date range, etc).

        Returns:
            List of matching opportunities.

        TODO: Implement opportunity search with keyword matching.
        """
        if self.opportunities_df is None:
            self.load_opportunities()

        logger.info("Available opportunity dataframe columns: %s", list(self.opportunities_df.columns))

        name_column = self._resolve_column("name", "title", "opportunity_name")
        skills_column = self._resolve_column("skills", "skill", "required_skills")

        if "name" not in self.opportunities_df.columns:
            logger.info(
                "'name' column not found in opportunities dataframe. Using '%s' as the opportunity name column.",
                name_column,
            )

        if not name_column:
            return []

        query = query or ""
        name_matches = self.opportunities_df[name_column].astype(str).str.contains(query, case=False, na=False)

        if skills_column:
            skills_matches = self.opportunities_df[skills_column].astype(str).str.contains(query, case=False, na=False)
            search_mask = name_matches | skills_matches
        else:
            search_mask = name_matches

        results = self.opportunities_df[search_mask]

        # Apply filters
        if filters:
            category_column = self._resolve_column("category")
            type_column = self._resolve_column("type", "category", "opportunity_type")

            if "category" in filters and category_column:
                results = results[results[category_column].astype(str).str.lower() == filters["category"].lower()]
            if "type" in filters and type_column:
                results = results[results[type_column].astype(str).str.lower() == filters["type"].lower()]

        type_column = self._resolve_column("type", "category", "opportunity_type")
        category_column = self._resolve_column("category")
        deadline_column = self._resolve_column("deadline", "date")
        link_column = self._resolve_column("application_link", "link")

        return [
            {
                "opportunity_name": row.get(name_column, ""),
                "opportunity_type": row.get(type_column, "") if type_column else "",
                "category": row.get(category_column, "") if category_column else "",
                "required_skills": [
                    skill.strip() for skill in str(row.get(skills_column, "")).split(",") if skill.strip()
                ]
                if skills_column
                else [],
                "deadline": row.get(deadline_column, "") if deadline_column else "",
                "application_link": row.get(link_column, "") if link_column else "",
            }
            for _, row in results.iterrows()
        ]

    def get_opportunity_details(self, opportunity_id: str) -> dict[str, Any]:
        """
        Get detailed information about an opportunity.

        Args:
            opportunity_id: Opportunity identifier.

        Returns:
            Dictionary with full opportunity details.

        TODO: Implement opportunity detail retrieval.
        """
        if self.opportunities_df is None:
            self.load_opportunities()

        opp = self.opportunities_df[self.opportunities_df["name"].str.lower() == opportunity_id.lower()]
        if opp.empty:
            return {}

        row = opp.iloc[0]
        return {
            "name": row.get("name", ""),
            "type": row.get("type", ""),
            "category": row.get("category", ""),
            "skills": row.get("skills", ""),
            "stipend": row.get("stipend", 0),
            "prize": row.get("prize", 0),
            "deadline": row.get("deadline", ""),
            "description": f"{row.get('type', '')} opportunity in {row.get('category', '')} field",
        }

    def filter_by_category(self, category: str) -> list[dict[str, Any]]:
        """
        Filter opportunities by category.

        Args:
            category: Opportunity category (internship, job, competition, etc).

        Returns:
            List of opportunities in specified category.

        TODO: Implement category filtering.
        """
        if self.opportunities_df is None:
            self.load_opportunities()

        filtered = self.opportunities_df[self.opportunities_df["type"].str.lower() == category.lower()]

        return [
            {
                "name": row.get("name", ""),
                "type": row.get("type", ""),
                "category": row.get("category", ""),
                "deadline": row.get("deadline", ""),
            }
            for _, row in filtered.iterrows()
        ]

    def filter_by_skill(self, skill: str) -> list[dict[str, Any]]:
        """
        Filter opportunities requiring specific skill.

        Args:
            skill: Required skill.

        Returns:
            List of opportunities requiring this skill.

        TODO: Implement skill-based filtering.
        """
        if self.opportunities_df is None:
            self.load_opportunities()

        filtered = self.opportunities_df[self.opportunities_df["skills"].str.contains(skill, case=False, na=False)]

        return [
            {
                "name": row.get("name", ""),
                "type": row.get("type", ""),
                "skills": row.get("skills", ""),
                "deadline": row.get("deadline", ""),
            }
            for _, row in filtered.iterrows()
        ]

    def get_upcoming_deadlines(self, days_ahead: int = 30) -> list[dict[str, Any]]:
        """
        Get opportunities with deadlines within specified days.

        Args:
            days_ahead: Number of days to look ahead.

        Returns:
            List of opportunities with upcoming deadlines.

        TODO: Implement deadline-based filtering.
        """
        if self.opportunities_df is None:
            self.load_opportunities()

        # For now, return all opportunities with deadlines
        upcoming = []
        for _, row in self.opportunities_df.iterrows():
            deadline = row.get("deadline", "")
            if deadline:
                upcoming.append(
                    {
                        "name": row.get("name", ""),
                        "type": row.get("type", ""),
                        "deadline": deadline,
                        "days_remaining": "Calculated based on deadline",
                    }
                )

        return upcoming
