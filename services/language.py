"""
Multilingual support module for Career Bridge AI.

Provides translation and language management for English, Hindi, and Telugu.
"""

from typing import Dict, Optional
from enum import Enum

class Language(str, Enum):
    """Supported languages."""
    ENGLISH = "English"
    HINDI = "हिंदी"
    TELUGU = "తెలుగు"


# Translation dictionary for UI elements
TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "app_title": {
        Language.ENGLISH: "🎓 Career Bridge AI",
        Language.HINDI: "🎓 कैरियर ब्रिज एआई",
        Language.TELUGU: "🎓 కెరీర్ బ్రిడ్జ్ ఎఐ"
    },
    "tagline": {
        Language.ENGLISH: "Your Personal Career Guidance Platform",
        Language.HINDI: "आपका व्यक्तिगत कैरियर मार्गदर्शन प्लेटफॉर्म",
        Language.TELUGU: "మీ ব్యక్తిగత కెరీర్ మార్గదర్శన ప్లాట్ఫర్మ్"
    },
    "home": {
        Language.ENGLISH: "Home",
        Language.HINDI: "होम",
        Language.TELUGU: "హోమ్"
    },
    "resume_analyzer": {
        Language.ENGLISH: "Resume Analyzer",
        Language.HINDI: "रिज्यूमे विश्लेषक",
        Language.TELUGU: "రెజ్యూమ్ విశ్లేషణ"
    },
    "career_mentor": {
        Language.ENGLISH: "Career Mentor",
        Language.HINDI: "कैरियर सलाहकार",
        Language.TELUGU: "కెరీర్ సలహా"
    },
    "scholarship_finder": {
        Language.ENGLISH: "Scholarship Finder",
        Language.HINDI: "छात्रवृत्ति खोज",
        Language.TELUGU: "స్కాలర్‌షిప్ ఖోజ"
    },
    "government_schemes": {
        Language.ENGLISH: "Government Schemes",
        Language.HINDI: "सरकारी योजनाएं",
        Language.TELUGU: "ప్రభుత్వ పథకాలు"
    },
    "opportunities": {
        Language.ENGLISH: "Opportunities",
        Language.HINDI: "अवसर",
        Language.TELUGU: "అవకాశాలు"
    },
    "learning_roadmap": {
        Language.ENGLISH: "Learning Roadmap",
        Language.HINDI: "सीखने का रोडमैप",
        Language.TELUGU: "లర్నింగ్ రోడ్‌మ్యాప్"
    },
    "ai_assistant": {
        Language.ENGLISH: "AI Career Assistant",
        Language.HINDI: "एआई कैरियर सहायक",
        Language.TELUGU: "ఎఐ కెరీర్ సహాయక"
    },
    "settings": {
        Language.ENGLISH: "Settings",
        Language.HINDI: "सेटिंग्स",
        Language.TELUGU: "సెట్టింగ్‌లు"
    },
    "language": {
        Language.ENGLISH: "Language",
        Language.HINDI: "भाषा",
        Language.TELUGU: "భాష"
    },
    "ai_provider": {
        Language.ENGLISH: "AI Provider",
        Language.HINDI: "एआई प्रदाता",
        Language.TELUGU: "ఎఐ ప్రదాతა"
    },
    "ollama": {
        Language.ENGLISH: "Ollama (Local)",
        Language.HINDI: "ओलामा (स्थानीय)",
        Language.TELUGU: "ఓలామా (స్థానిక)"
    },
    "byok": {
        Language.ENGLISH: "BYOK (Bring Your Own Key)",
        Language.HINDI: "बीवाईओके (अपनी कुंजी लाएं)",
        Language.TELUGU: "బిఎయోకె (మీ స్వంత కీ తీసుకుండండి)"
    },
    "api_key": {
        Language.ENGLISH: "API Key / Token",
        Language.HINDI: "एपीआई कुंजी / टोकन",
        Language.TELUGU: "ఎపిఐ కీ / టోకన్"
    },
    "model_name": {
        Language.ENGLISH: "Model Name",
        Language.HINDI: "मॉडल नाम",
        Language.TELUGU: "మోడల్ పేరు"
    },
    "ask_question": {
        Language.ENGLISH: "Ask a Career Question",
        Language.HINDI: "कैरियर प्रश्न पूछें",
        Language.TELUGU: "కెరీర్ ప్రశ్న అడగండి"
    },
    "generate_roadmap": {
        Language.ENGLISH: "Generate Career Roadmap",
        Language.HINDI: "कैरियर रोडमैप बनाएं",
        Language.TELUGU: "కెరీర్ రోడ్‌మ్యాప్ ఉత్పత్తి చేయండి"
    },
    "resume_tips": {
        Language.ENGLISH: "Resume Improvement Tips",
        Language.HINDI: "रिज्यूमे सुधार सुझाव",
        Language.TELUGU: "రెజ్యూమ్ మెరుగుదల చిట్కాలు"
    },
    "interview_questions": {
        Language.ENGLISH: "Interview Questions",
        Language.HINDI: "साक्षात्कार प्रश्न",
        Language.TELUGU: "ఇంటర్వ్యూ ప్రశ్నలు"
    },
    "skill_recommendations": {
        Language.ENGLISH: "Skill Recommendations",
        Language.HINDI: "कौशल सिफारिशें",
        Language.TELUGU: "నైపుణ్య సిఫారసులు"
    },
    "project_suggestions": {
        Language.ENGLISH: "Project Suggestions",
        Language.HINDI: "परियोजना सुझाव",
        Language.TELUGU: "ప్రాజెక్ట్ సూచనలు"
    },
    "save": {
        Language.ENGLISH: "Save",
        Language.HINDI: "बचाएं",
        Language.TELUGU: "సేవ్ చేయండి"
    },
    "cancel": {
        Language.ENGLISH: "Cancel",
        Language.HINDI: "रद्द करें",
        Language.TELUGU: "రద్దు చేయండి"
    },
    "error": {
        Language.ENGLISH: "Error",
        Language.HINDI: "त्रुटि",
        Language.TELUGU: "లోపం"
    },
    "success": {
        Language.ENGLISH: "Success",
        Language.HINDI: "सफल",
        Language.TELUGU: "విజయం"
    },
    "loading": {
        Language.ENGLISH: "Loading...",
        Language.HINDI: "लोड हो रहा है...",
        Language.TELUGU: "లోడ్ చేస్తోంది..."
    },
    "ollama_not_running": {
        Language.ENGLISH: "❌ Ollama is not running. Please start Ollama first: http://localhost:11434",
        Language.HINDI: "❌ ओलामा चल नहीं रहा है। कृपया पहले ओलामा शुरू करें: http://localhost:11434",
        Language.TELUGU: "❌ ఓలామా నడుస్తోంది కాదు. దయచేసి ఓలామాను ఆరంభించండి: http://localhost:11434"
    },
    "ollama_connection_error": {
        Language.ENGLISH: "❌ Failed to connect to Ollama. Make sure it's running on port 11434.",
        Language.HINDI: "❌ ओलामा से जुड़ने में विफल। सुनिश्चित करें कि यह पोर्ट 11434 पर चल रहा है।",
        Language.TELUGU: "❌ ఓలామాకు కనెక్ట్ చేయడంలో విఫలమైంది. ఇది పోర్ట్ 11434 నుండి నడుస్తోందని నిర్ధారించుకోండి."
    },
    "invalid_api_key": {
        Language.ENGLISH: "❌ Invalid API Key. Please check your BYOK settings.",
        Language.HINDI: "❌ अमान्य एपीआई कुंजी। कृपया अपनी बीवाईओके सेटिंग्स की जांच करें।",
        Language.TELUGU: "❌ చెల్లని ఎపిఐ కీ. దయచేసి మీ బిఎయోకె సెట్టింగ్‌లను తనిఖీ చేయండి."
    }
}


def get_text(key: str, language: Language = Language.ENGLISH) -> str:
    """
    Get translated text for a key.
    
    Args:
        key: Translation key
        language: Target language
        
    Returns:
        Translated text or key if translation not found
    """
    if key in TRANSLATIONS:
        return TRANSLATIONS[key].get(language, TRANSLATIONS[key].get(Language.ENGLISH, key))
    return key


def translate_response(response: str, target_language: Language) -> str:
    """
    Translate AI response to target language.
    
    For full implementation, would use translation API.
    Currently returns original response.
    
    Args:
        response: Original response text
        target_language: Target language
        
    Returns:
        Translated response
        
    TODO: Integrate with translation service (Google Translate API, etc.)
    """
    if target_language == Language.ENGLISH:
        return response
    
    # Placeholder for translation logic
    # In production, use Google Translate API, Azure Translator, etc.
    return response


def get_supported_languages() -> Dict[str, Language]:
    """
    Get all supported languages.
    
    Returns:
        Dictionary mapping language names to Language enum
    """
    return {
        "English": Language.ENGLISH,
        "हिंदी": Language.HINDI,
        "తెలుగు": Language.TELUGU
    }
