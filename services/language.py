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

DEFAULT_LANGUAGE = "English"

UI_TRANSLATIONS = {
    "English": {
        "navigation": "Navigation",
        "home": "Home",
        "resume_analyzer": "Resume Analyzer",
        "career_mentor": "Career Mentor",
        "scholarship_finder": "Scholarship Finder",
        "government_schemes": "Government Schemes",
        "opportunities": "Opportunities",
        "learning_roadmap": "Learning Roadmap",
        "ai_career_assistant": "AI Career Assistant",
        "quick_links": "Quick Links",
        "language": "Response Language",
        "resume_header": "Resume Analyzer",
        "resume_subtitle": "Upload your resume for analysis",
        "resume_upload": "Upload your resume (PDF, DOCX, TXT)",
        "resume_spinner": "Analyzing your resume...",
        "resume_success": "Resume analyzed successfully!",
        "resume_extract_error": "Could not extract text from the resume. Please upload a readable PDF/DOCX.",
        "resume_format_error": "Please upload a resume in PDF, DOCX, or TXT format.",
        "resume_general_error": "Resume analysis failed. Please try another readable PDF/DOCX/TXT file.",
        "extracted_skills": "Extracted Skills",
        "career_suggestions": "Career Suggestions",
        "skill_gaps": "Skill Gaps",
        "recommended_learning_path": "Recommended Learning Path",
        "education": "Education",
        "work_experience": "Work Experience",
        "improvement_suggestions": "Improvement Suggestions",
        "no_skills_detected": "No skills detected. You can still get fallback career guidance below.",
        "no_education": "No education information found.",
        "no_experience": "No work experience found.",
        "suggest_keywords": "Add more keywords from your industry.",
        "suggest_skills": "Include more specific technical skills.",
        "suggest_education": "Add your educational background.",
        "suggest_experience": "Include your work experience.",
        "resume_good": "Great job! Your resume looks good.",
        "career_header": "Career Mentor",
        "career_subtitle": "Get personalized career recommendations",
        "your_profile": "Your Profile",
        "years_experience": "Years of Experience",
        "education_level": "Education Level",
        "career_domain": "Career Domain",
        "your_skills": "Your Skills",
        "get_recommendations": "Get Career Recommendations",
        "recommendation_spinner": "Generating career recommendations...",
        "recommendation_success": "Found career recommendations!",
        "recommendation_fallback": "Recommendation engine had an issue, so we generated a safe rule-based recommendation.",
        "recommendation_prompt": "Add your skills and click Get Career Recommendations to see suggestions.",
        "match_score": "Match Score",
        "growth_potential": "Growth Potential",
        "salary_range": "Salary Range",
        "required_skills": "Required Skills",
        "matching_skills": "Matching Skills",
        "suggested_next_steps": "Suggested Next Steps",
        "rule_based_fallback": "Rule-based fallback",
        "learn_more": "Learn More",
        "not_available": "Not available",
    },
    "Telugu": {
        "navigation": "నావిగేషన్",
        "home": "హోమ్",
        "resume_analyzer": "రెజ్యూమే విశ్లేషణ",
        "career_mentor": "కెరీర్ మెంటర్",
        "scholarship_finder": "స్కాలర్‌షిప్ ఫైండర్",
        "government_schemes": "ప్రభుత్వ పథకాలు",
        "opportunities": "అవకాశాలు",
        "learning_roadmap": "లెర్నింగ్ రోడ్‌మ్యాప్",
        "ai_career_assistant": "AI కెరీర్ అసిస్టెంట్",
        "quick_links": "త్వరిత లింకులు",
        "language": "స్పందన భాష",
        "resume_header": "రెజ్యూమే విశ్లేషణ",
        "resume_subtitle": "విశ్లేషణ కోసం మీ రెజ్యూమేను అప్లోడ్ చేయండి",
        "resume_upload": "మీ రెజ్యూమేను అప్లోడ్ చేయండి (PDF, DOCX, TXT)",
        "resume_spinner": "మీ రెజ్యూమేను విశ్లేషిస్తున్నాం...",
        "resume_success": "రెజ్యూమే విజయవంతంగా విశ్లేషించబడింది!",
        "resume_extract_error": "రెజ్యూమే నుండి టెక్స్ట్ తీసుకోలేకపోయాం. చదవగలిగే PDF/DOCX అప్లోడ్ చేయండి.",
        "resume_format_error": "దయచేసి PDF, DOCX, లేదా TXT ఫార్మాట్‌లో రెజ్యూమే అప్లోడ్ చేయండి.",
        "resume_general_error": "రెజ్యూమే విశ్లేషణ విఫలమైంది. మరో చదవగలిగే ఫైల్ ప్రయత్నించండి.",
        "extracted_skills": "గుర్తించిన నైపుణ్యాలు",
        "career_suggestions": "కెరీర్ సూచనలు",
        "skill_gaps": "స్కిల్ గ్యాప్స్",
        "recommended_learning_path": "సిఫార్సు చేసిన లెర్నింగ్ పాత్",
        "education": "విద్య",
        "work_experience": "పని అనుభవం",
        "improvement_suggestions": "మెరుగుదల సూచనలు",
        "no_skills_detected": "నైపుణ్యాలు గుర్తించబడలేదు. అయినా క్రింద కెరీర్ మార్గదర్శనం పొందవచ్చు.",
        "no_education": "విద్యా సమాచారం కనబడలేదు.",
        "no_experience": "పని అనుభవం కనబడలేదు.",
        "suggest_keywords": "మీ రంగానికి సంబంధించిన keywords చేర్చండి.",
        "suggest_skills": "మరిన్ని స్పష్టమైన టెక్నికల్ స్కిల్స్ చేర్చండి.",
        "suggest_education": "మీ విద్యా వివరాలు చేర్చండి.",
        "suggest_experience": "మీ పని అనుభవాన్ని చేర్చండి.",
        "resume_good": "బాగుంది! మీ రెజ్యూమే మంచి స్థితిలో ఉంది.",
        "career_header": "కెరీర్ మెంటర్",
        "career_subtitle": "వ్యక్తిగత కెరీర్ సిఫార్సులు పొందండి",
        "your_profile": "మీ ప్రొఫైల్",
        "years_experience": "అనుభవం సంవత్సరాలు",
        "education_level": "విద్యా స్థాయి",
        "career_domain": "కెరీర్ రంగం",
        "your_skills": "మీ నైపుణ్యాలు",
        "get_recommendations": "కెరీర్ సిఫార్సులు పొందండి",
        "recommendation_spinner": "కెరీర్ సిఫార్సులు రూపొందిస్తున్నాం...",
        "recommendation_success": "కెరీర్ సిఫార్సులు దొరికాయి!",
        "recommendation_fallback": "సిఫార్సు ఇంజిన్‌లో సమస్య వచ్చింది, కాబట్టి సురక్షిత rule-based సిఫార్సు రూపొందించాం.",
        "recommendation_prompt": "మీ నైపుణ్యాలు ఎంచుకుని కెరీర్ సిఫార్సులు పొందండి.",
        "match_score": "మ్యాచ్ స్కోర్",
        "growth_potential": "వృద్ధి అవకాశం",
        "salary_range": "జీతం పరిధి",
        "required_skills": "అవసరమైన నైపుణ్యాలు",
        "matching_skills": "సరిపోయే నైపుణ్యాలు",
        "suggested_next_steps": "తదుపరి చర్యలు",
        "rule_based_fallback": "Rule-based fallback",
        "learn_more": "ఇంకా తెలుసుకోండి",
        "not_available": "లభ్యం లేదు",
    },
}


def get_language_names() -> list[str]:
    """Return display names for supported languages."""
    return list(SUPPORTED_LANGUAGES.keys())


def normalize_language(language: str | None) -> str:
    """Return a supported language name with a safe fallback."""
    if language in SUPPORTED_LANGUAGES:
        return language
    return DEFAULT_LANGUAGE


def get_language_instruction(language: str) -> str:
    """Return an instruction that can be added to an AI prompt."""
    return SUPPORTED_LANGUAGES[normalize_language(language)]["instruction"]


def get_language_code(language: str) -> str:
    """Return a stable language code for a supported language."""
    return SUPPORTED_LANGUAGES[normalize_language(language)]["code"]


def translate(key: str, language: str | None = None) -> str:
    """Translate UI labels with English fallback for missing Telugu text."""
    selected = normalize_language(language)
    return UI_TRANSLATIONS.get(selected, {}).get(key) or UI_TRANSLATIONS["English"].get(key, key)


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
