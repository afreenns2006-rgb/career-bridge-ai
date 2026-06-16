from pathlib import Path

from career_engine import CareerRecommendationEngine
from resume_parser import ResumeParser


class FakeUpload:
    def __init__(self, name: str, content: bytes) -> None:
        self.name = name
        self._content = content

    def getvalue(self) -> bytes:
        return self._content


def test_txt_resume_extracts_skills_and_text(tmp_path: Path) -> None:
    resume = tmp_path / "resume.txt"
    resume.write_text(
        "A fresher with Python, SQL, data analysis, HTML, CSS, Git, and communication skills.",
        encoding="utf-8",
    )

    parser = ResumeParser(resume)

    assert parser.validate_resume()
    assert "Python" in parser.extract_text()
    skills = parser.extract_skills()
    assert "python" in skills
    assert "sql" in skills


def test_streamlit_upload_resume_parses_without_local_file_path() -> None:
    upload = FakeUpload(
        "resume.txt",
        b"Python SQL Excel data analysis bachelor degree projects",
    )

    parser = ResumeParser.from_upload(upload)

    assert parser.validate_resume()
    assert "Python" in parser.extract_text()
    assert {"python", "sql"}.issubset(set(parser.extract_skills()))


def test_career_recommendations_never_return_unknown() -> None:
    engine = CareerRecommendationEngine()

    recommendations = engine.recommend_careers(
        user_skills=["python", "sql", "data analysis"],
        education="UG",
        experience_years=0,
        preferences={"domain": "Data"},
    )

    assert recommendations
    assert all(rec["career_name"] and rec["career_name"] != "Unknown" for rec in recommendations)
    assert recommendations[0]["required_skills"]
    assert recommendations[0]["learning_roadmap"]


def test_career_fallback_returns_meaningful_role_for_empty_profile() -> None:
    engine = CareerRecommendationEngine()

    recommendations = engine.generate_fallback_recommendations(
        user_skills=[],
        education="Not provided",
        experience_years=0,
        preferences={},
    )

    assert recommendations[0]["career_name"] in {
        "Data Analyst",
        "Python Developer",
        "Web Developer",
        "AI/ML Beginner",
        "Software Tester",
        "Full Stack Developer",
        "Software Developer",
    }
    assert recommendations[0]["missing_skills"]


def test_career_fallback_mappings_match_required_demo_roles() -> None:
    engine = CareerRecommendationEngine()

    cases = [
        (["Python", "SQL", "Excel"], {}, "Data Analyst"),
        (["HTML", "CSS", "JavaScript"], {}, "Web Developer"),
        (["Java", "C", "Programming"], {}, "Software Developer"),
        ([], {"interests": "general tech interest"}, "AI/ML Beginner"),
    ]

    for skills, preferences, expected_role in cases:
        recommendations = engine.generate_fallback_recommendations(
            user_skills=skills,
            education="UG",
            experience_years=0,
            preferences=preferences,
        )
        assert recommendations[0]["career_name"] == expected_role
        assert recommendations[0]["learning_roadmap"]
