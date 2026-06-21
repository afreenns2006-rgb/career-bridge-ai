"""
Scholarship recommendation engine for Career Bridge AI.

Provides scholarship opportunities based on user eligibility criteria,
academic profile, and preferences.
"""

from typing import Any, Optional
import logging
import pandas as pd

from database import get_db_manager
from config import SCHOLARSHIPS_CSV

logger = logging.getLogger(__name__)

# Default scholarships database
DEFAULT_SCHOLARSHIPS = [
    {
        "name": "Google Scholarship",
        "award": 50000,
        "education": "UG",
        "max_income": 800000,
        "category": "merit",
        "deadline": "2026-07-31",
    },
    {
        "name": "Microsoft Scholarship",
        "award": 40000,
        "education": "UG,PG",
        "max_income": 1000000,
        "category": "merit",
        "deadline": "2026-08-15",
    },
    {
        "name": "National Merit Scholarship",
        "award": 30000,
        "education": "12th",
        "max_income": 600000,
        "category": "merit",
        "deadline": "2026-06-30",
    },
    {
        "name": "SC/ST Scholarship",
        "award": 25000,
        "education": "UG,PG",
        "max_income": 500000,
        "category": "need-based",
        "deadline": "2026-09-30",
    },
    {
        "name": "Women In Tech Scholarship",
        "award": 35000,
        "education": "UG",
        "max_income": 900000,
        "category": "merit",
        "deadline": "2026-08-01",
    },
]


class ScholarshipRecommendationEngine:
    """
    Generates scholarship recommendations based on user profile.

    Analyzes eligibility criteria including education level, state,
    income, and academic performance to suggest suitable scholarships.
    """

    def __init__(self) -> None:
        """
        Initialize scholarship recommendation engine.

        TODO: Implement engine initialization.
        """
        self.scholarships_df: Optional[pd.DataFrame] = None
        self.db_manager = get_db_manager()
        self.load_scholarships()

    def load_scholarships(self) -> pd.DataFrame:
        """
        Load scholarships database from CSV.

        Returns:
            DataFrame with scholarship details and eligibility criteria.

        TODO: Implement scholarship data loading from SCHOLARSHIPS_CSV.
        """
        try:
            if SCHOLARSHIPS_CSV.exists():
                self.scholarships_df = pd.read_csv(SCHOLARSHIPS_CSV)
            else:
                self.scholarships_df = pd.DataFrame(DEFAULT_SCHOLARSHIPS)
        except Exception as e:
            logger.warning(f"Could not load scholarships CSV: {e}. Using defaults.")
            self.scholarships_df = pd.DataFrame(DEFAULT_SCHOLARSHIPS)

        return self.scholarships_df

    def recommend_scholarships(
        self,
        education_level: str,
        state: str,
        annual_income: float,
        gpa: Optional[float] = None,
        preferences: Optional[dict[str, Any]] = None,
    ) -> list[dict[str, Any]]:
        """
        Generate scholarship recommendations for user.

        Args:
            education_level: Current education level (10th, 12th, UG, PG).
            state: State of residence.
            annual_income: Annual family income.
            gpa: Grade Point Average (optional).
            preferences: Optional preferences for scholarship type.

        Returns:
            List of eligible scholarship recommendations with details.

        TODO: Implement scholarship recommendation algorithm using:
            - Education level filtering
            - Income eligibility
            - State eligibility
            - Academic criteria
            - Application deadlines
        """
        if self.scholarships_df is None:
            self.load_scholarships()

        recommendations = []

        for _, scholarship_row in self.scholarships_df.iterrows():
            scholarship_name = scholarship_row.get("name", "")
            education_list = str(scholarship_row.get("education", "")).split(",")
            max_income = scholarship_row.get("max_income", float("inf"))

            # Check eligibility
            education_match = any(edu.strip().lower() == education_level.lower() for edu in education_list)
            income_match = annual_income <= max_income

            if education_match and income_match:
                # Calculate match score
                score = 75 + (100 - (annual_income / max_income * 100) if max_income > 0 else 0) * 0.25
                if gpa and gpa >= 3.5:
                    score += 10

                recommendations.append(
                    {
                        "scholarship_name": scholarship_name,
                        "award_amount": scholarship_row.get("award", 0),
                        "match_score": round(min(score, 100), 1),
                        "category": scholarship_row.get("category", "general"),
                        "eligibility": "Eligible",
                        "deadline": scholarship_row.get("deadline", "Not specified"),
                        "education_level": scholarship_row.get("education", ""),
                    }
                )

        return sorted(recommendations, key=lambda x: x.get("match_score", 0), reverse=True)

    def check_eligibility(self, scholarship_id: str, user_profile: dict[str, Any]) -> dict[str, Any]:
        """
        Check eligibility for specific scholarship.

        Args:
            scholarship_id: Scholarship identifier.
            user_profile: User profile with eligibility criteria.

        Returns:
            Dictionary with eligibility status and reasons.

        TODO: Implement eligibility checking.
        """
        if self.scholarships_df is None:
            self.load_scholarships()

        scholarship = self.scholarships_df[self.scholarships_df["name"].str.lower() == scholarship_id.lower()]
        if scholarship.empty:
            return {"eligible": False, "reason": "Scholarship not found"}

        row = scholarship.iloc[0]
        reasons = []
        eligible = True

        # Check education level
        education_list = str(row.get("education", "")).split(",")
        if user_profile.get("education_level") not in education_list:
            eligible = False
            reasons.append("Education level does not match")

        # Check income
        if user_profile.get("annual_income", 0) > row.get("max_income", float("inf")):
            eligible = False
            reasons.append("Income exceeds maximum limit")

        return {
            "eligible": eligible,
            "scholarship_name": row.get("name", ""),
            "reasons": reasons if not eligible else ["You are eligible for this scholarship"],
        }

    def get_scholarship_details(self, scholarship_id: str) -> dict[str, Any]:
        """
        Get detailed information about a scholarship.

        Args:
            scholarship_id: Scholarship identifier.

        Returns:
            Dictionary with scholarship details, requirements, application info.

        TODO: Implement scholarship detail retrieval.
        """
        if self.scholarships_df is None:
            self.load_scholarships()

        scholarship = self.scholarships_df[self.scholarships_df["name"].str.lower() == scholarship_id.lower()]
        if scholarship.empty:
            return {}

        row = scholarship.iloc[0]
        return {
            "name": row.get("name", ""),
            "award": row.get("award", 0),
            "category": row.get("category", ""),
            "education_level": row.get("education", ""),
            "max_income": row.get("max_income", 0),
            "deadline": row.get("deadline", ""),
            "description": f"Scholarship for {row.get('category', '')} students",
        }

    def get_application_timeline(self, scholarship_id: str) -> dict[str, Any]:
        """
        Get application timeline and important dates.

        Args:
            scholarship_id: Scholarship identifier.

        Returns:
            Dictionary with application dates and deadlines.

        TODO: Implement timeline retrieval.
        """
        scholarship = self.get_scholarship_details(scholarship_id)
        if not scholarship:
            return {}

        return {
            "scholarship_name": scholarship.get("name", ""),
            "application_start": "2026-05-01",
            "application_deadline": scholarship.get("deadline", ""),
            "result_announcement": "2026-10-01",
            "disbursement": "2026-11-01",
        }

    def filter_by_category(self, category: str) -> list[dict[str, Any]]:
        """
        Filter scholarships by category.

        Args:
            category: Scholarship category (merit-based, need-based, etc).

        Returns:
            List of scholarships in specified category.

        TODO: Implement category filtering.
        """
        if self.scholarships_df is None:
            self.load_scholarships()

        filtered = self.scholarships_df[self.scholarships_df["category"].str.lower() == category.lower()]

        return [
            {
                "name": row.get("name", ""),
                "award": row.get("award", 0),
                "category": row.get("category", ""),
                "deadline": row.get("deadline", ""),
            }
            for _, row in filtered.iterrows()
        ]
