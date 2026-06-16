from services.ai_provider import AIProviderConfig, build_career_assistant_prompt, generate_ai_response
from services.language import get_language_instruction, get_language_names, translate


def test_supported_languages_include_required_options() -> None:
    languages = get_language_names()

    assert "English" in languages
    assert "Hindi" in languages
    assert "Telugu" in languages


def test_ui_translation_uses_selected_language_and_fallback() -> None:
    assert translate("resume_analyzer", "Hindi") == "रिज्यूमे विश्लेषक"
    assert translate("resume_analyzer", "Telugu") == "రెజ్యూమే విశ్లేషణ"
    assert translate("missing_key", "Hindi") == "missing_key"


def test_prompt_uses_selected_language_instruction() -> None:
    prompt = build_career_assistant_prompt(
        "How do I become a data analyst?",
        "Hindi",
        {"education_level": "UG", "experience_years": 0, "skills": ["Python", "SQL"]},
    )

    assert get_language_instruction("Hindi") in prompt
    assert "Python, SQL" in prompt


def test_rule_based_fallback_returns_selected_language_content() -> None:
    response = generate_ai_response(
        "Suggest projects",
        AIProviderConfig(provider="Rule-based fallback", language="Telugu"),
        {},
    )

    assert "కెరీర్" in response
