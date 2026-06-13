"""Language helpers for Career Bridge AI."""

SUPPORTED_LANGUAGES = {
    "English": {
        "code": "en",
        "instruction": "Respond in clear, beginner-friendly English.",
    },
    "Hindi": {
        "code": "hi",
        "instruction": "Respond in Hindi using Devanagari script. Keep the tone simple and supportive.",
    },
    "Telugu": {
        "code": "te",
        "instruction": "Respond in Telugu script. Keep the tone simple and supportive.",
    },
}


def get_language_names() -> list[str]:
    """Return display names for supported languages."""
    return list(SUPPORTED_LANGUAGES.keys())


def get_language_instruction(language: str) -> str:
    """Return an instruction that can be added to an AI prompt."""
    return SUPPORTED_LANGUAGES.get(language, SUPPORTED_LANGUAGES["English"])["instruction"]


def build_rule_based_response(question: str, language: str) -> str:
    """Create a safe local response when no AI provider is available."""
    if language == "Hindi":
        return f"""
### करियर रोडमैप
1. अपना लक्ष्य रोल चुनें और उसके लिए जरूरी कौशल लिखें।
2. 30 दिन तक बुनियादी कौशल सीखें, फिर छोटे प्रोजेक्ट बनाएं।
3. हर सप्ताह रिज्यूमे और LinkedIn/GitHub प्रोफाइल अपडेट करें।

### रिज्यूमे सुधार सुझाव
- उपलब्धियों को संख्या के साथ लिखें।
- हर प्रोजेक्ट में समस्या, तकनीक और परिणाम बताएं।
- जॉब विवरण से मिलते-जुलते कीवर्ड जोड़ें।

### इंटरव्यू प्रश्न
- अपने सबसे अच्छे प्रोजेक्ट को समझाइए।
- आपने कौन सी समस्या हल की और कैसे?
- आपकी सबसे मजबूत तकनीकी स्किल कौन सी है?

### स्किल और प्रोजेक्ट सुझाव
- Python, SQL, communication और problem solving मजबूत करें।
- एक portfolio project, एक data analysis project और एक deployment project बनाएं।

**आपका सवाल:** {question}
"""

    if language == "Telugu":
        return f"""
### కెరీర్ రోడ్‌మ్యాప్
1. మీ లక్ష్య పాత్రను ఎంచుకుని, అవసరమైన నైపుణ్యాలను రాయండి.
2. 30 రోజులు ప్రాథమిక నైపుణ్యాలు నేర్చుకుని, చిన్న ప్రాజెక్టులు చేయండి.
3. ప్రతి వారం రెజ్యూమే మరియు LinkedIn/GitHub ప్రొఫైల్‌ను అప్డేట్ చేయండి.

### రెజ్యూమే మెరుగుదల సూచనలు
- సాధించిన విషయాలను సంఖ్యలతో చూపండి.
- ప్రతి ప్రాజెక్టులో సమస్య, టెక్నాలజీ, ఫలితాన్ని వివరించండి.
- ఉద్యోగ వివరణకు సరిపోయే keywords చేర్చండి.

### ఇంటర్వ్యూ ప్రశ్నలు
- మీ ఉత్తమ ప్రాజెక్టును వివరించండి.
- మీరు ఏ సమస్యను ఎలా పరిష్కరించారు?
- మీ బలమైన టెక్నికల్ స్కిల్ ఏమిటి?

### స్కిల్ మరియు ప్రాజెక్ట్ సూచనలు
- Python, SQL, communication, problem solving నైపుణ్యాలను బలపరచండి.
- ఒక portfolio project, ఒక data analysis project, ఒక deployment project చేయండి.

**మీ ప్రశ్న:** {question}
"""

    return f"""
### Career Roadmap
1. Pick one target role and list the skills it requires.
2. Spend 30 days on foundations, then build small proof-of-work projects.
3. Update your resume and LinkedIn/GitHub profile every week.

### Resume Improvement Tips
- Add numbers to achievements wherever possible.
- For every project, explain the problem, technology used, and result.
- Add keywords from the job descriptions you are targeting.

### Interview Questions
- Walk me through your strongest project.
- What problem did you solve and why did you choose that approach?
- Which technical skill are you strongest in, and how have you used it?

### Skill and Project Suggestions
- Strengthen Python, SQL, communication, and problem solving.
- Build one portfolio project, one data analysis project, and one deployed application.

**Your question:** {question}
"""
