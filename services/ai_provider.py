"""AI provider integrations for Career Bridge AI."""

from dataclasses import dataclass
from typing import Any

import requests

from services.language import build_rule_based_response, get_language_instruction

OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"
DEFAULT_OLLAMA_MODEL = "llama3"
DEFAULT_BYOK_ENDPOINT = "https://api.openai.com/v1/chat/completions"
DEFAULT_BYOK_MODEL = "gpt-4o-mini"


@dataclass
class AIProviderConfig:
    """Runtime AI provider settings from the Streamlit UI."""

    provider: str
    language: str
    model_name: str = DEFAULT_OLLAMA_MODEL
    ollama_url: str = OLLAMA_GENERATE_URL
    api_token: str = ""
    byok_endpoint: str = DEFAULT_BYOK_ENDPOINT


def build_career_assistant_prompt(question: str, language: str, profile: dict[str, Any] | None = None) -> str:
    """Build a focused career-assistant prompt."""
    profile = profile or {}
    skills = profile.get("skills") or []
    education_level = profile.get("education_level") or "not provided"
    experience_years = profile.get("experience_years", "not provided")

    return f"""
You are Career Bridge AI, a friendly career mentor for students.
{get_language_instruction(language)}

Use the student's context:
- Education level: {education_level}
- Experience years: {experience_years}
- Skills: {", ".join(skills) if skills else "not provided"}

Answer the user's career question and include these sections:
1. Career roadmap
2. Resume improvement tips
3. Interview questions
4. Skill recommendations
5. Project suggestions

Keep the answer practical, beginner-friendly, and specific.

User question:
{question}
""".strip()


def generate_ai_response(question: str, config: AIProviderConfig, profile: dict[str, Any] | None = None) -> str:
    """Generate a career assistant response using the selected provider."""
    if not question.strip():
        return "Please enter a career-related question first."

    prompt = build_career_assistant_prompt(question, config.language, profile)

    if config.provider == "Local Ollama":
        return _generate_with_ollama(prompt, config)

    if config.provider == "BYOK":
        return _generate_with_byok(prompt, config)

    return build_rule_based_response(question, config.language)


def _generate_with_ollama(prompt: str, config: AIProviderConfig) -> str:
    """Call the local Ollama generate API."""
    try:
        response = requests.post(
            config.ollama_url,
            json={
                "model": config.model_name or DEFAULT_OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
            },
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip() or "Ollama returned an empty response. Please try again."
    except requests.exceptions.ConnectionError:
        return (
            "I could not connect to Ollama. Please start Ollama locally, run "
            f"`ollama pull {config.model_name or DEFAULT_OLLAMA_MODEL}`, and try again."
        )
    except requests.exceptions.Timeout:
        return "Ollama took too long to respond. Please try again or use a smaller local model."
    except requests.exceptions.RequestException as exc:
        return f"Ollama returned an error: {exc}"
    except ValueError:
        return "Ollama returned an invalid response. Please check the local Ollama server."


def _generate_with_byok(prompt: str, config: AIProviderConfig) -> str:
    """Call an OpenAI-compatible chat completions endpoint with a user-provided token."""
    if not config.api_token:
        return "Please enter your BYOK API key/token in the sidebar before generating an AI response."

    try:
        response = requests.post(
            config.byok_endpoint or DEFAULT_BYOK_ENDPOINT,
            headers={
                "Authorization": f"Bearer {config.api_token}",
                "Content-Type": "application/json",
            },
            json={
                "model": config.model_name or DEFAULT_BYOK_MODEL,
                "messages": [
                    {"role": "system", "content": "You are Career Bridge AI, a helpful career mentor."},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.4,
            },
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        choices = data.get("choices", [])
        if choices:
            return choices[0].get("message", {}).get("content", "").strip()
        return "The BYOK provider returned an empty response. Please check your model and endpoint."
    except requests.exceptions.ConnectionError:
        return "I could not reach the BYOK provider endpoint. Please check the URL and your internet connection."
    except requests.exceptions.Timeout:
        return "The BYOK provider took too long to respond. Please try again."
    except requests.exceptions.HTTPError as exc:
        return f"BYOK provider returned an HTTP error: {exc}"
    except requests.exceptions.RequestException as exc:
        return f"BYOK provider returned an error: {exc}"
    except ValueError:
        return "The BYOK provider returned an invalid response. Please check the endpoint format."
