"""
Government scheme recommendation engine for Career Bridge AI.

Provides Indian government scheme recommendations based on eligibility
criteria including state, education, income, and age.
"""

from typing import List, Dict, Any, Optional
import logging
import pandas as pd

from database import get_db_manager
from config import SCHEMES_CSV

logger = logging.getLogger(__name__)

# Default government schemes database
DEFAULT_SCHEMES = [
    {
        "name": "Prime Minister Skill Development Scheme",
        "type": "skill_development",
        "benefit": "Free training + Rs 8000",
        "max_income": 1000000,
        "age_limit": 45,
        "states": "All",
        "deadline": "Rolling",
    },
    {
        "name": "National Apprenticeship Promotion Scheme",
        "type": "apprenticeship",
        "benefit": "Apprenticeship stipend",
        "max_income": 1200000,
        "age_limit": 50,
        "states": "All",
        "deadline": "Rolling",
    },
    {
        "name": "PMEGP Scheme",
        "type": "business",
        "benefit": "Loan up to 25 lakhs",
        "max_income": 1500000,
        "age_limit": 65,
        "states": "All",
        "deadline": "Rolling",
    },
    {
        "name": "SC/ST Scholarship",
        "type": "scholarship",
        "benefit": "Rs 50000 per year",
        "max_income": 600000,
        "age_limit": 25,
        "states": "All",
        "deadline": "2026-09-30",
    },
    {
        "name": "State Scholarship for Merit Students",
        "type": "merit_scholarship",
        "benefit": "Rs 30000 per year",
        "max_income": 800000,
        "age_limit": 25,
        "states": "Multiple",
        "deadline": "2026-08-31",
    },
]


class GovernmentSchemeEngine:
    """
    Generates government scheme recommendations.

    Analyzes eligibility based on state, education level, income,
    and age to recommend suitable government assistance schemes.
    """

    def __init__(self) -> None:
        """
        Initialize government scheme recommendation engine.

        TODO: Implement engine initialization.
        """
        self.schemes_df: Optional[pd.DataFrame] = None
        self.db_manager = get_db_manager()
        self.load_schemes()

    def load_schemes(self) -> pd.DataFrame:
        """
        Load government schemes database from CSV.

        Returns:
            DataFrame with government schemes and eligibility criteria.

        TODO: Implement scheme data loading from SCHEMES_CSV.
        """
        try:
            if SCHEMES_CSV.exists():
                self.schemes_df = pd.read_csv(SCHEMES_CSV)
            else:
                self.schemes_df = pd.DataFrame(DEFAULT_SCHEMES)
        except Exception as e:
            logger.warning(f"Could not load schemes CSV: {e}. Using defaults.")
            self.schemes_df = pd.DataFrame(DEFAULT_SCHEMES)

        return self.schemes_df

    def recommend_schemes(
        self,
        state: str,
        education_level: str,
        annual_income: float,
        age: int,
        category: Optional[str] = None,
        preferences: Optional[dict[str, Any]] = None,
    ) -> list[dict[str, Any]]:
        """
        Generate government scheme recommendations for user.

        Args:
            state: State of residence (Indian state).
            education_level: Current education level.
            annual_income: Annual family income.
            age: Age of applicant.
            category: Social category (General, OBC, SC, ST).
            preferences: Optional scheme type preferences.

        Returns:
            List of eligible government scheme recommendations.

        TODO: Implement scheme recommendation algorithm using:
            - State eligibility
            - Education level filtering
            - Income eligibility
            - Age eligibility
            - Social category eligibility
            - Application deadlines
        """
        if self.schemes_df is None:
            self.load_schemes()

        recommendations = []

        for _, scheme_row in self.schemes_df.iterrows():
            scheme_name = scheme_row.get("name", "")
            max_income = scheme_row.get("max_income", float("inf"))
            age_limit = scheme_row.get("age_limit", 100)

            # Check eligibility
            income_match = annual_income <= max_income
            age_match = age <= age_limit

            if income_match and age_match:
                score = 75
                if category and "SC/ST" in scheme_name and category in ["SC", "ST"]:
                    score += 15

                recommendations.append(
                    {
                        "scheme_name": scheme_name,
                        "scheme_type": scheme_row.get("type", ""),
                        "benefit": scheme_row.get("benefit", ""),
                        "match_score": score,
                        "eligibility": "Eligible",
                        "deadline": scheme_row.get("deadline", "Rolling"),
                        "max_income": max_income,
                        "age_limit": age_limit,
                    }
                )

        return sorted(recommendations, key=lambda x: x.get("match_score", 0), reverse=True)

    def check_scheme_eligibility(self, scheme_id: str, user_profile: dict[str, Any]) -> dict[str, Any]:
        """
        Check eligibility for specific government scheme.

        Args:
            scheme_id: Scheme identifier.
            user_profile: User profile with eligibility criteria.

        Returns:
            Dictionary with eligibility status and requirements.

        TODO: Implement eligibility checking.
        """
        if self.schemes_df is None:
            self.load_schemes()

        scheme = self.schemes_df[self.schemes_df["name"].str.lower() == scheme_id.lower()]
        if scheme.empty:
            return {"eligible": False, "reason": "Scheme not found"}

        row = scheme.iloc[0]
        reasons = []
        eligible = True

        # Check income
        if user_profile.get("annual_income", 0) > row.get("max_income", float("inf")):
            eligible = False
            reasons.append(f"Income exceeds limit of {row.get('max_income')}")

        # Check age
        if user_profile.get("age", 0) > row.get("age_limit", 100):
            eligible = False
            reasons.append(f"Age exceeds limit of {row.get('age_limit')}")

        return {
            "eligible": eligible,
            "scheme_name": row.get("name", ""),
            "reasons": reasons if not eligible else ["You are eligible for this scheme"],
        }

    def get_scheme_details(self, scheme_id: str) -> dict[str, Any]:
        """
        Get detailed information about a government scheme.

        Args:
            scheme_id: Scheme identifier.

        Returns:
            Dictionary with scheme details, benefits, application process.

        TODO: Implement scheme detail retrieval.
        """
        if self.schemes_df is None:
            self.load_schemes()

        scheme = self.schemes_df[self.schemes_df["name"].str.lower() == scheme_id.lower()]
        if scheme.empty:
            return {}

        row = scheme.iloc[0]
        return {
            "name": row.get("name", ""),
            "type": row.get("type", ""),
            "benefit": row.get("benefit", ""),
            "max_income": row.get("max_income", 0),
            "age_limit": row.get("age_limit", 0),
            "deadline": row.get("deadline", ""),
            "description": f"Government {row.get('type', '')} scheme",
        }

    def get_application_process(self, scheme_id: str) -> dict[str, Any]:
        """
        Get application process details for a scheme.

        Args:
            scheme_id: Scheme identifier.

        Returns:
            Dictionary with step-by-step application instructions.

        TODO: Implement application process retrieval.
        """
        return {
            "step_1": "Verify eligibility criteria",
            "step_2": "Gather required documents",
            "step_3": "Complete application form",
            "step_4": "Submit to government office",
            "step_5": "Track application status",
            "estimated_processing_time": "30-60 days",
        }

    def get_required_documents(self, scheme_id: str) -> list[str]:
        """
        Get list of required documents for scheme application.

        Args:
            scheme_id: Scheme identifier.

        Returns:
            List of required documents.

        TODO: Implement required documents retrieval.
        """
        return [
            "Aadhar Card",
            "Pan Card",
            "Educational Certificate",
            "Income Certificate",
            "Bank Passbook",
            "Address Proof",
            "Recent Photograph",
        ]

    def filter_by_state(self, state: str) -> list[dict[str, Any]]:
        """
        Filter schemes by state.

        Args:
            state: State name.

        Returns:
            List of schemes available in specified state.

        TODO: Implement state-based filtering.
        """
        if self.schemes_df is None:
            self.load_schemes()

        # Schemes marked as "All" are available everywhere
        filtered = self.schemes_df[
            (self.schemes_df["states"].str.contains("All", case=False, na=False))
            | (self.schemes_df["states"].str.contains(state, case=False, na=False))
        ]

        return [
            {
                "name": row.get("name", ""),
                "type": row.get("type", ""),
                "benefit": row.get("benefit", ""),
                "deadline": row.get("deadline", ""),
            }
            for _, row in filtered.iterrows()
        ]
