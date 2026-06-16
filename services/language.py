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
    },
    "welcome_message": {
        Language.ENGLISH: "Welcome to Career Bridge AI - Your Personal Career Guidance Platform",
        Language.HINDI: "कैरियर ब्रिज एआई में आपका स्वागत है - आपका व्यक्तिगत कैरियर मार्गदर्शन प्लेटफॉर्म",
        Language.TELUGU: "కెరీర్ బ్రిడ్జ్ ఎఐకి స్వాగతం - మీ ব్యక్తిగత కెరీర్ మార్గదర్శన ప్లాట్ఫర్మ్"
    },
    "bridging_students": {
        Language.ENGLISH: "Bridging Students to Opportunities",
        Language.HINDI: "छात्रों को अवसरों से जोड़ना",
        Language.TELUGU: "విద్యార్థులను అవకాశాలకు అనుసంధానించడం"
    },
    "career_guidance": {
        Language.ENGLISH: "Career Bridge AI is an intelligent platform that helps you navigate your career journey with:",
        Language.HINDI: "कैरियर ब्रिज एआई एक बुद्धिमान प्लेटफॉर्म है जो आपको अपनी कैरियर यात्रा नेविगेट करने में मदद करता है:",
        Language.TELUGU: "కెరీర్ బ్రిడ్జ్ ఎఐ ఒక తెలివైన ప్లాట్ఫర్మ్ ఇది మీ కెరీర్ ప్రయాణాన్ని నావిగేట్ చేయడానికి సహాయం చేస్తుంది:"
    },
    "resume_analyzer_desc": {
        Language.ENGLISH: "📄 Resume Analyzer\nGet AI-powered analysis of your resume with ATS scoring and improvement suggestions.",
        Language.HINDI: "📄 रिज्यूमे विश्लेषक\nएआई-संचालित विश्लेषण प्राप्त करें एटीएस स्कोरिंग और सुधार सुझाव के साथ।",
        Language.TELUGU: "📄 రెజ్యూమ్ విశ్లేషణ\nఎఐ-శక్తితో కూడిన విశ్లేషణ పొందండి ఎటిఎస్ స్కోరింగ్ మరియు మెరుగుదల సూచనలు."
    },
    "career_recommendations_desc": {
        Language.ENGLISH: "💼 Career Recommendations\nDiscover career paths that match your skills and experience with detailed guidance.",
        Language.HINDI: "💼 कैरियर सिफारिशें\nकौशल और अनुभव से मेल खाने वाले कैरियर पथ खोजें।",
        Language.TELUGU: "💼 కెరీర్ సిఫారసులు\nనిపుణత మరియు అనుభవంతో సరిపోలిన కెరీర్ పాతను కనుగొనండి."
    },
    "scholarship_finder_desc": {
        Language.ENGLISH: "🎓 Scholarship Finder\nFind and apply for scholarships matching your eligibility criteria.",
        Language.HINDI: "🎓 छात्रवृत्ति खोज\nअपनी पात्रता मानदंड से मेल खाने वाली छात्रवृत्ति खोजें और आवेदन करें।",
        Language.TELUGU: "🎓 స్కాలర్‌షిప్ ఖోజ\nమీ అర్హత ప్రమాణాలకు సరిపోలిన స్కాలర్‌షిప్‌ల కోసం ఖోజ చేయండి మరియు దరఖాస్తు చేయండి."
    },
    "government_schemes_desc": {
        Language.ENGLISH: "🏛️ Government Schemes\nAccess information about government schemes and assistance programs.",
        Language.HINDI: "🏛️ सरकारी योजनाएं\nसरकारी योजनाओं और सहायता कार्यक्रमों के बारे में जानकारी प्राप्त करें।",
        Language.TELUGU: "🏛️ ప్రభుత్వ పథకాలు\nప్రభుత్వ పథకాలు మరియు సహాయ కార్యక్రమాల గురించిన సమాచారాన్ని యాక్సెస్ చేయండి."
    },
    "opportunities_desc": {
        Language.ENGLISH: "🚀 Opportunities\nExplore internships, competitions, and career-building opportunities.",
        Language.HINDI: "🚀 अवसर\nइंटर्नशिप, प्रतियोगिताएं और कैरियर निर्माण के अवसरों का अन्वेषण करें।",
        Language.TELUGU: "🚀 అవకాశాలు\nఇంటర్న్‌షిప్‌లు, పోటీలు మరియు కెరీర్-నిర్మాణ అవకాశాలను అన్వేషించండి."
    },
    "learning_roadmap_desc": {
        Language.ENGLISH: "🗺️ Learning Roadmap\nCreate personalized learning paths to bridge your skill gaps.",
        Language.HINDI: "🗺️ सीखने का रोडमैप\nअपने कौशल अंतराल को पाटने के लिए व्यक्तिगत सीखने के पथ बनाएं।",
        Language.TELUGU: "🗺️ లర్నింగ్ రోడ్‌మ్యాప్\nమీ నైపుణ్య అంతరాలను పూరించడానికి ব్যక్తిగతకృత సిద్ధాంత పాతను సృష్టించండి."
    },
    "platform_statistics": {
        Language.ENGLISH: "Platform Statistics",
        Language.HINDI: "प्लेटफॉर्म आंकड़े",
        Language.TELUGU: "ప్లాట్ఫర్మ్ గణాంకాలు"
    },
    "active_users": {
        Language.ENGLISH: "Active Users",
        Language.HINDI: "सक्रिय उपयोगकर्ता",
        Language.TELUGU: "సక్రియ వినియోగదారులు"
    },
    "total_opportunities": {
        Language.ENGLISH: "Opportunities",
        Language.HINDI: "अवसर",
        Language.TELUGU: "అవకాశాలు"
    },
    "total_scholarships": {
        Language.ENGLISH: "Scholarships",
        Language.HINDI: "छात्रवृत्ति",
        Language.TELUGU: "స్కాలర్‌షిప్‌లు"
    },
    "success_rate": {
        Language.ENGLISH: "Success Rate",
        Language.HINDI: "सफलता दर",
        Language.TELUGU: "విజయ రేటు"
    },
    "getting_started": {
        Language.ENGLISH: "Getting Started",
        Language.HINDI: "शुरुआत करना",
        Language.TELUGU: "ప్రారంభం చేయడం"
    },
    "quick_links": {
        Language.ENGLISH: "Quick Links",
        Language.HINDI: "त्वरित लिंक",
        Language.TELUGU: "శీఘ్ర లింకులు"
    },
    "documentation": {
        Language.ENGLISH: "Documentation",
        Language.HINDI: "दस्तावेज़",
        Language.TELUGU: "డాక్యుమెంటేషన్"
    },
    "report_issue": {
        Language.ENGLISH: "Report Issue",
        Language.HINDI: "समस्या की रिपोर्ट करें",
        Language.TELUGU: "సమస్యను నివేదించండి"
    },
    "contact_us": {
        Language.ENGLISH: "Contact Us",
        Language.HINDI: "हमसे संपर्क करें",
        Language.TELUGU: "మమ్మల్ని సంప్రదించండి"
    },
    "upload_resume": {
        Language.ENGLISH: "Upload your resume for analysis",
        Language.HINDI: "विश्लेषण के लिए अपना रिज्यूमे अपलोड करें",
        Language.TELUGU: "విశ్లేషణ కోసం మీ రెజ్యూమ్ అప్‌లోడ్ చేయండి"
    },
    "upload_file": {
        Language.ENGLISH: "Upload your resume (PDF, DOCX, TXT)",
        Language.HINDI: "अपना रिज्यूमे अपलोड करें (पीडीएफ, डीओসीएक्स, टीएक्सटी)",
        Language.TELUGU: "మీ రెజ్యూమ్ అప్‌లోడ్ చేయండి (PDF, DOCX, TXT)"
    },
    "invalid_resume": {
        Language.ENGLISH: "❌ Invalid resume. Please upload a valid resume file.",
        Language.HINDI: "❌ अमान्य रिज्यूमे। कृपया एक वैध रिज्यूमे फ़ाइल अपलोड करें।",
        Language.TELUGU: "❌ చెల్లని రెజ్యూమ్. దయచేసి చెల్లుబాటు చేసిన రెజ్యూమ్ ఫైలును అప్‌లోడ్ చేయండి."
    },
    "analyzing_resume": {
        Language.ENGLISH: "Analyzing your resume...",
        Language.HINDI: "आपके रिज्यूमे का विश्लेषण कर रहे हैं...",
        Language.TELUGU: "మీ రెజ్యూమ్‌ను విశ్లేషిస్తోంది..."
    },
    "resume_analyzed": {
        Language.ENGLISH: "✅ Resume analyzed successfully!",
        Language.HINDI: "✅ रिज्यूमे सफलतापूर्वक विश्लेषित!",
        Language.TELUGU: "✅ రెజ్యూమ్ విజయవంతంగా విశ్లేషించబడింది!"
    },
    "ats_score": {
        Language.ENGLISH: "ATS Score",
        Language.HINDI: "एटीएस स्कोर",
        Language.TELUGU: "ఎటిఎస్ స్కోర్"
    },
    "skills_found": {
        Language.ENGLISH: "Skills Found",
        Language.HINDI: "कौशल मिला",
        Language.TELUGU: "కనిపించిన నైపుణ్యాలు"
    },
    "education_label": {
        Language.ENGLISH: "Education",
        Language.HINDI: "शिक्षा",
        Language.TELUGU: "విద్య"
    },
    "extracted_skills": {
        Language.ENGLISH: "Extracted Skills",
        Language.HINDI: "निकाले गए कौशल",
        Language.TELUGU: "సంగ్రహించిన నైపుణ్యాలు"
    },
    "no_skills_detected": {
        Language.ENGLISH: "No skills detected. Please ensure your resume contains your skills.",
        Language.HINDI: "कोई कौशल पता नहीं चला। कृपया सुनिश्चित करें कि आपका रिज्यूमे आपके कौशल को शामिल करता है।",
        Language.TELUGU: "ఎటువంటి నైపుణ్యాలు కనుగొనబడలేదు. దయచేసి మీ రెజ్యూమ్ మీ నైపుణ్యాలను కలిగి ఉన్నందని నిర్ధారించుకోండి."
    },
    "work_experience": {
        Language.ENGLISH: "Work Experience",
        Language.HINDI: "कार्य अनुभव",
        Language.TELUGU: "కార్య అనుభవం"
    },
    "no_education_found": {
        Language.ENGLISH: "No education information found.",
        Language.HINDI: "कोई शिक्षा जानकारी नहीं मिली।",
        Language.TELUGU: "విద్య సమాచారం కనుగొనబడలేదు."
    },
    "no_experience_found": {
        Language.ENGLISH: "No work experience found.",
        Language.HINDI: "कोई कार्य अनुभव नहीं मिला।",
        Language.TELUGU: "కార్య అనుభవం కనుగొనబడలేదు."
    },
    "improvement_suggestions": {
        Language.ENGLISH: "Improvement Suggestions",
        Language.HINDI: "सुधार सुझाव",
        Language.TELUGU: "మెరుగుదల సూచనలు"
    },
    "resume_looks_good": {
        Language.ENGLISH: "Great job! Your resume looks good.",
        Language.HINDI: "बहुत बढ़िया! आपका रिज्यूमे अच्छा लग रहा है।",
        Language.TELUGU: "చేసిన ఉత్తమ పని! మీ రెజ్యూమ్ బాగానే ఉంది."
    },
    "personalized_recommendations": {
        Language.ENGLISH: "Get personalized career recommendations",
        Language.HINDI: "व्यक्तिगत कैरियर सिफारिशें प्राप्त करें",
        Language.TELUGU: "ఆ కేంద్రీకృత కెరీర్ సిఫారసులను పొందండి"
    },
    "your_profile": {
        Language.ENGLISH: "Your Profile",
        Language.HINDI: "आपकी प्रोफ़ाइल",
        Language.TELUGU: "మీ ప్రొఫైల్"
    },
    "years_of_experience": {
        Language.ENGLISH: "Years of Experience",
        Language.HINDI: "अनुभव के वर्ष",
        Language.TELUGU: "అనుభవ సంవత్సరాలు"
    },
    "education_level": {
        Language.ENGLISH: "Education Level",
        Language.HINDI: "शिक्षा स्तर",
        Language.TELUGU: "విద్య స్థితి"
    },
    "your_skills": {
        Language.ENGLISH: "Your Skills",
        Language.HINDI: "आपके कौशल",
        Language.TELUGU: "మీ నైపుణ్యాలు"
    },
    "get_career_recommendations": {
        Language.ENGLISH: "Get Career Recommendations",
        Language.HINDI: "कैरियर सिफारिशें प्राप्त करें",
        Language.TELUGU: "కెరీర్ సిఫారసులను పొందండి"
    },
    "career_recommendations_found": {
        Language.ENGLISH: "Found {count} career recommendations!",
        Language.HINDI: "{count} कैरियर सिफारिशें मिलीं!",
        Language.TELUGU: "{count} కెరీర్ సిఫారసులు కనుగొనబడ్డాయి!"
    },
    "match_score": {
        Language.ENGLISH: "Match Score",
        Language.HINDI: "मैच स्कोर",
        Language.TELUGU: "మ్యాచ్ స్కోర్"
    },
    "salary_range": {
        Language.ENGLISH: "Salary Range",
        Language.HINDI: "वेतन सीमा",
        Language.TELUGU: "జీతం శ్రేణి"
    },
    "growth_potential": {
        Language.ENGLISH: "Growth Potential",
        Language.HINDI: "वृद्धि संभावना",
        Language.TELUGU: "వృద్ధి సామర్థ్యం"
    },
    "matching_skills": {
        Language.ENGLISH: "Matching Skills",
        Language.HINDI: "मेलखाते कौशल",
        Language.TELUGU: "సరిపోలిన నైపుణ్యాలు"
    },
    "skills_to_learn": {
        Language.ENGLISH: "Skills to Learn",
        Language.HINDI: "सीखने के लिए कौशल",
        Language.TELUGU: "నేర్చుకోవలసిన నైపుణ్యాలు"
    },
    "learn_more": {
        Language.ENGLISH: "Learn More",
        Language.HINDI: "और जानें",
        Language.TELUGU: "మరిన్ని తెలుసుకోండి"
    },
    "no_recommendations": {
        Language.ENGLISH: "No career recommendations found. Please add more skills to your profile.",
        Language.HINDI: "कोई कैरियर सिफारिशें नहीं मिलीं। कृपया अपनी प्रोफ़ाइल में अधिक कौशल जोड़ें।",
        Language.TELUGU: "కెరీర్ సిఫారసులు కనుగొనబడలేదు. దయచేసి మీ ప్రొఫైల్‌కు మరిన్ని నైపుణ్యాలను జోడించండి."
    },
    "discover_scholarships": {
        Language.ENGLISH: "Discover scholarship opportunities",
        Language.HINDI: "छात्रवृत्ति के अवसरों की खोज करें",
        Language.TELUGU: "స్కాలర్‌షిప్ అవకాశాలను కనుగొనండి"
    },
    "your_details": {
        Language.ENGLISH: "Your Details",
        Language.HINDI: "आपके विवरण",
        Language.TELUGU: "మీ వివరాలు"
    },
    "state": {
        Language.ENGLISH: "State",
        Language.HINDI: "राज्य",
        Language.TELUGU: "రాష్ట్రం"
    },
    "annual_income": {
        Language.ENGLISH: "Annual Family Income (₹)",
        Language.HINDI: "वार्षिक पारिवारिक आय (₹)",
        Language.TELUGU: "వార్షిక కుటుంబ ఆదాయం (₹)"
    },
    "gpa": {
        Language.ENGLISH: "GPA (if available)",
        Language.HINDI: "जीपीए (यदि उपलब्ध हो)",
        Language.TELUGU: "జిపిఎ (అందుబాటులో ఉంటే)"
    },
    "find_scholarships": {
        Language.ENGLISH: "Find Scholarships",
        Language.HINDI: "छात्रवृत्ति खोजें",
        Language.TELUGU: "స్కాలర్‌షిప్‌లను కనుగొనండి"
    },
    "scholarships_found": {
        Language.ENGLISH: "Found {count} matching scholarships!",
        Language.HINDI: "{count} मेलखाती छात्रवृत्तियां मिलीं!",
        Language.TELUGU: "{count} సరిపోలిన స్కాలర్‌షిప్‌లు కనుగొనబడ్డాయి!"
    },
    "award_amount": {
        Language.ENGLISH: "Award Amount",
        Language.HINDI: "पुरस्कार राशि",
        Language.TELUGU: "పురస్కార రాశి"
    },
    "eligibility": {
        Language.ENGLISH: "Eligibility",
        Language.HINDI: "योग्यता",
        Language.TELUGU: "అర్హత"
    },
    "deadline": {
        Language.ENGLISH: "Deadline",
        Language.HINDI: "समय सीमा",
        Language.TELUGU: "గడువు"
    },
    "apply_now": {
        Language.ENGLISH: "Apply Now",
        Language.HINDI: "अभी आवेदन करें",
        Language.TELUGU: "ఇప్పుడే దరఖాస్తు చేయండి"
    },
    "no_scholarships": {
        Language.ENGLISH: "No scholarships found matching your criteria. Try adjusting your details.",
        Language.HINDI: "आपके मानदंड से मेल खाती कोई छात्रवृत्ति नहीं मिली। अपने विवरण को समायोजित करने का प्रयास करें।",
        Language.TELUGU: "మీ ప్రమాణాలకు సరిపోలిన స్కాలర్‌షిప్‌లు కనుగొనబడలేదు. మీ వివరాలను సర్దుబాటు చేయటానికి ప్రయత్నించండి."
    },
    "government_scheme_desc": {
        Language.ENGLISH: "Find relevant government schemes",
        Language.HINDI: "प्रासंगिक सरकारी योजनाएं खोजें",
        Language.TELUGU: "సంబంధిత ప్రభుత్వ పథకాలను కనుగొనండి"
    },
    "age": {
        Language.ENGLISH: "Age",
        Language.HINDI: "आयु",
        Language.TELUGU: "వయస్సు"
    },
    "social_category": {
        Language.ENGLISH: "Social Category",
        Language.HINDI: "सामाजिक श्रेणी",
        Language.TELUGU: "సామాజిక వర్గం"
    },
    "select_category": {
        Language.ENGLISH: "Select your social category for eligibility",
        Language.HINDI: "पात्रता के लिए अपनी सामाजिक श्रेणी का चयन करें",
        Language.TELUGU: "అర్హతకు మీ సామాజిక వర్గాన్ని ఎంచుకోండి"
    },
    "get_scheme_recommendations": {
        Language.ENGLISH: "Get Scheme Recommendations",
        Language.HINDI: "योजना सिफारिशें प्राप्त करें",
        Language.TELUGU: "పథక సిఫారసులను పొందండి"
    },
    "schemes_found": {
        Language.ENGLISH: "Found {count} eligible government schemes!",
        Language.HINDI: "{count} पात्र सरकारी योजनाएं मिलीं!",
        Language.TELUGU: "{count} అర్హతకు సరిపడే ప్రభుత్వ పథకాలు కనుగొనబడ్డాయి!"
    },
    "scheme_type": {
        Language.ENGLISH: "Type",
        Language.HINDI: "प्रकार",
        Language.TELUGU: "రకం"
    },
    "benefit": {
        Language.ENGLISH: "Benefit",
        Language.HINDI: "लाभ",
        Language.TELUGU: "ప్రయోజనం"
    },
    "max_income": {
        Language.ENGLISH: "Max Income",
        Language.HINDI: "अधिकतम आय",
        Language.TELUGU: "గరిష్ట ఆదాయం"
    },
    "age_limit": {
        Language.ENGLISH: "Age Limit",
        Language.HINDI: "आयु सीमा",
        Language.TELUGU: "వయస్సు పరిమితి"
    },
    "application_process": {
        Language.ENGLISH: "Application Process",
        Language.HINDI: "आवेदन प्रक्रिया",
        Language.TELUGU: "దరఖాస్తు ప్రక్రియ"
    },
    "required_documents": {
        Language.ENGLISH: "Required Documents",
        Language.HINDI: "आवश्यक दस्तावेज़",
        Language.TELUGU: "అవసరమైన డాక్యుమెంట్‌లు"
    },
    "no_schemes": {
        Language.ENGLISH: "No government schemes found matching your criteria.",
        Language.HINDI: "आपके मानदंड से मेल खाती कोई सरकारी योजना नहीं मिली।",
        Language.TELUGU: "మీ ప్రమాణాలకు సరిపోలిన ప్రభుత్వ పథకాలు కనుగొనబడలేదు."
    },
    "explore_opportunities": {
        Language.ENGLISH: "Explore career opportunities",
        Language.HINDI: "कैरियर अवसरों का अन्वेषण करें",
        Language.TELUGU: "కెరీర్ అవకాశాలను అన్వేషించండి"
    },
    "search_opportunities": {
        Language.ENGLISH: "Search opportunities",
        Language.HINDI: "अवसरों की खोज करें",
        Language.TELUGU: "అవకాశాలను కనుగొనండి"
    },
    "search_placeholder": {
        Language.ENGLISH: "e.g., internship, python, data science",
        Language.HINDI: "जैसे, इंटर्नशिप, पायथन, डेटा विज्ञान",
        Language.TELUGU: "ఉదా, ఇంటర్న్‌షిప్, పైథాన్, డేటా సైన్స్"
    },
    "type": {
        Language.ENGLISH: "Type",
        Language.HINDI: "प्रकार",
        Language.TELUGU: "రకం"
    },
    "category": {
        Language.ENGLISH: "Category",
        Language.HINDI: "श्रेणी",
        Language.TELUGU: "వర్గం"
    },
    "opportunities_found": {
        Language.ENGLISH: "Found {count} opportunities!",
        Language.HINDI: "{count} अवसर मिले!",
        Language.TELUGU: "{count} అవకాశాలు కనుగొనబడ్డాయి!"
    },
    "opportunity_type": {
        Language.ENGLISH: "Type",
        Language.HINDI: "प्रकार",
        Language.TELUGU: "రకం"
    },
    "match_score_label": {
        Language.ENGLISH: "Match Score",
        Language.HINDI: "मैच स्कोर",
        Language.TELUGU: "మ్యాచ్ స్కోర్"
    },
    "stipend_prize": {
        Language.ENGLISH: "Stipend/Prize",
        Language.HINDI: "वजीफा/पुरस्कार",
        Language.TELUGU: "వేతనం/పురస్కారం"
    },
    "required_skills": {
        Language.ENGLISH: "Required Skills",
        Language.HINDI: "आवश्यक कौशल",
        Language.TELUGU: "అవసరమైన నైపుణ్యాలు"
    },
    "redirecting": {
        Language.ENGLISH: "Redirecting to application...",
        Language.HINDI: "आवेदन पर पुनर्निर्देशित हो रहे हैं...",
        Language.TELUGU: "అప్లికేషన్‌కు పునర్నిర్దేశించబడుతోంది..."
    },
    "no_opportunities": {
        Language.ENGLISH: "No opportunities found. Try adjusting your filters or search query.",
        Language.HINDI: "कोई अवसर नहीं मिले। अपने फ़िल्टर या खोज क्वेरी को समायोजित करने का प्रयास करें।",
        Language.TELUGU: "ఎటువంటి అవకాశాలు కనుగొనబడలేదు. మీ ఫిల్టర్‌లు లేదా సెర్చ్ క్వెరీని సర్దుబాటు చేయటానికి ప్రయత్నించండి."
    },
    "create_learning_roadmap": {
        Language.ENGLISH: "Create your personalized learning roadmap",
        Language.HINDI: "अपना व्यक्तिगत सीखने का रोडमैप बनाएं",
        Language.TELUGU: "మీ ఆ కేంద్రీకృత సిద్ధాంత రోడ్‌మ్యాప్ సృష్టించండి"
    },
    "target_career": {
        Language.ENGLISH: "Target Career",
        Language.HINDI: "लक्ष्य कैरियर",
        Language.TELUGU: "లక్ష్య కెరీర్"
    },
    "available_hours": {
        Language.ENGLISH: "Available Hours per Week",
        Language.HINDI: "प्रति सप्ताह उपलब्ध घंटे",
        Language.TELUGU: "వారానికి అందుబాటులో ఉన్న గంటలు"
    },
    "learning_duration": {
        Language.ENGLISH: "Learning Duration (months)",
        Language.HINDI: "सीखने की अवधि (महीने)",
        Language.TELUGU: "సిద్ధాంత వ్యవధి (నెలలు)"
    },
    "preferred_pace": {
        Language.ENGLISH: "Preferred Pace",
        Language.HINDI: "पसंदीदा गति",
        Language.TELUGU: "ఇష్ట గति"
    },
    "generate_roadmap": {
        Language.ENGLISH: "Generate Learning Roadmap",
        Language.HINDI: "सीखने का रोडमैप बनाएं",
        Language.TELUGU: "సిద్ధాంత రోడ్‌మ్యాప్ ఉత్పత్తి చేయండి"
    },
    "roadmap_generated": {
        Language.ENGLISH: "✅ Roadmap generated successfully!",
        Language.HINDI: "✅ रोडमैप सफलतापूर्वक बनाया गया!",
        Language.TELUGU: "✅ రోడ్‌మ్యాప్ విజయవంతంగా ఉత్పత్తి చేయబడింది!"
    },
    "duration": {
        Language.ENGLISH: "Duration",
        Language.HINDI: "अवधि",
        Language.TELUGU: "వ్యవధి"
    },
    "weekly_hours": {
        Language.ENGLISH: "Weekly Hours",
        Language.HINDI: "साप्ताहिक घंटे",
        Language.TELUGU: "వారానిక గంటలు"
    },
    "total_hours": {
        Language.ENGLISH: "Total Hours",
        Language.HINDI: "कुल घंटे",
        Language.TELUGU: "మొత్తం గంటలు"
    },
    "skill_gap_analysis": {
        Language.ENGLISH: "Skill Gap Analysis",
        Language.HINDI: "कौशल अंतराल विश्लेषण",
        Language.TELUGU: "నైపుణ్య అంతర విశ్లేషణ"
    },
    "current_skills": {
        Language.ENGLISH: "Current Skills",
        Language.HINDI: "वर्तमान कौशल",
        Language.TELUGU: "ప్రస్తుత నైపుణ్యాలు"
    },
    "target_skills": {
        Language.ENGLISH: "Target Skills",
        Language.HINDI: "लक्ष्य कौशल",
        Language.TELUGU: "లక్ష్య నైపుణ్యాలు"
    },
    "monthly_breakdown": {
        Language.ENGLISH: "Monthly Breakdown",
        Language.HINDI: "मासिक विभाजन",
        Language.TELUGU: "నెలవారీ విభజన"
    },
    "estimated_hours": {
        Language.ENGLISH: "Estimated Hours",
        Language.HINDI: "अनुमानित घंटे",
        Language.TELUGU: "అంచనా వేసిన గంటలు"
    },
    "skills_to_develop": {
        Language.ENGLISH: "Skills to Develop",
        Language.HINDI: "विकसित करने के लिए कौशल",
        Language.TELUGU: "అభివృద్ధి చేయవలసిన నైపుణ్యాలు"
    },
    "recommended_resources": {
        Language.ENGLISH: "Recommended Resources",
        Language.HINDI: "अनुशंसित संसाधन",
        Language.TELUGU: "సిఫార్సు చేసిన వనరులు"
    },
    "download_roadmap": {
        Language.ENGLISH: "Download Roadmap (PDF)",
        Language.HINDI: "रोडमैप डाउनलोड करें (पीडीएफ)",
        Language.TELUGU: "రోడ్‌మ్యాప్ డౌన్‌లోడ్ చేయండి (PDF)"
    },
    "start_learning": {
        Language.ENGLISH: "Start Learning",
        Language.HINDI: "सीखना शुरू करें",
        Language.TELUGU: "సిద్ధాంత ప్రారంభించండి"
    },
    "share_roadmap": {
        Language.ENGLISH: "Share Roadmap",
        Language.HINDI: "रोडमैप साझा करें",
        Language.TELUGU: "రోడ్‌మ్యాప్ భాగస్వామ్యం చేయండి"
    },
    "ai_assistant_desc": {
        Language.ENGLISH: "Ask career-related questions and get AI-powered insights",
        Language.HINDI: "कैरियर से संबंधित प्रश्न पूछें और एआई-संचालित अंतर्दृष्टि प्राप्त करें",
        Language.TELUGU: "కెరీర్-సంబంధిత ప్రశ్నలను అడగండి మరియు ఎఐ-శక్తితో కూడిన ఇన్‌సైట్‌లను పొందండి"
    },
    "question": {
        Language.ENGLISH: "Your question:",
        Language.HINDI: "आपका सवाल:",
        Language.TELUGU: "మీ ప్రశ్న:"
    },
    "question_placeholder": {
        Language.ENGLISH: "e.g., How can I transition from web development to machine learning?",
        Language.HINDI: "उदाहरण: मैं वेब डेवलपमेंट से मशीन लर्निंग में कैसे संक्रमण कर सकता हूं?",
        Language.TELUGU: "ఉదా, నేను వెబ్ డెవలప్‌మెంట్ నుండి మెషిన్ లర్నింగ్‌కు ఎలా మారవచ్చు?"
    },
    "get_ai_response": {
        Language.ENGLISH: "Get AI Response",
        Language.HINDI: "एआई प्रतिक्रिया प्राप्त करें",
        Language.TELUGU: "ఎఐ ప్రతిస్పందనను పొందండి"
    },
    "ai_response": {
        Language.ENGLISH: "✅ AI Response:",
        Language.HINDI: "✅ एआई प्रतिक्रिया:",
        Language.TELUGU: "✅ ఎఐ ప్రతిస్పందన:"
    },
    "enter_question": {
        Language.ENGLISH: "Please enter a question.",
        Language.HINDI: "कृपया एक प्रश्न दर्ज करें।",
        Language.TELUGU: "దయచేసి ఒక ప్రశ్నను నమోదు చేయండి."
    },
    "generate_career_roadmap": {
        Language.ENGLISH: "Generate Career Roadmap",
        Language.HINDI: "कैरियर रोडमैप बनाएं",
        Language.TELUGU: "కెరీర్ రోడ్‌మ్యాప్ ఉత్పత్తి చేయండి"
    },
    "target_career_label": {
        Language.ENGLISH: "Target career:",
        Language.HINDI: "लक्ष्य कैरियर:",
        Language.TELUGU: "లక్ష్య కెరీర్:"
    },
    "target_career_placeholder": {
        Language.ENGLISH: "e.g., Data Scientist",
        Language.HINDI: "जैसे, डेटा वैज्ञानिक",
        Language.TELUGU: "ఉదా, డేటా సైంటిస్ట్"
    },
    "current_level": {
        Language.ENGLISH: "Current skill level:",
        Language.HINDI: "वर्तमान कौशल स्तर:",
        Language.TELUGU: "ప్రస్తుత నైపుణ్య స్థితి:"
    },
    "timeline": {
        Language.ENGLISH: "Timeline (months):",
        Language.HINDI: "समयरेखा (महीने):",
        Language.TELUGU: "సమయ రేఖ (నెలలు):"
    },
    "ai_roadmap_generated": {
        Language.ENGLISH: "✅ AI-Generated Roadmap:",
        Language.HINDI: "✅ एआई-उत्पन्न रोडमैप:",
        Language.TELUGU: "✅ ఎఐ-ఉత్పత్తి చేసిన రోడ్‌మ్యాప్:"
    },
    "enter_target_career": {
        Language.ENGLISH: "Please enter a target career.",
        Language.HINDI: "कृपया एक लक्ष्य कैरियर दर्ज करें।",
        Language.TELUGU: "దయచేసి లక్ష్య కెరీర్‌ను నమోదు చేయండి."
    },
    "resume_improvement": {
        Language.ENGLISH: "Get Resume Improvement Tips",
        Language.HINDI: "रिज्यूमे सुधार सुझाव प्राप्त करें",
        Language.TELUGU: "రెజ్యూమ్ మెరుగుదల చిట్కాలను పొందండి"
    },
    "upload_analyze_resume": {
        Language.ENGLISH: "Please upload and analyze your resume first in the Resume Analyzer section.",
        Language.HINDI: "कृपया पहले रिज्यूमे विश्लेषक अनुभाग में अपना रिज्यूमे अपलोड और विश्लेषण करें।",
        Language.TELUGU: "దయచేసి రెజ్యూమ్ విశ్లేషణ విభాగంలో ఎక్కడ మీ రెజ్యూమ్‌ను అప్‌లోడ్ చేసి విశ్లేషించండి."
    },
    "analyze_resume": {
        Language.ENGLISH: "Analyze My Resume",
        Language.HINDI: "मेरे रिज्यूमे का विश्लेषण करें",
        Language.TELUGU: "నా రెజ్యూమ్‌ను విశ్లేషించండి"
    },
    "resume_tips": {
        Language.ENGLISH: "✅ Resume Improvement Tips:",
        Language.HINDI: "✅ रिज्यूमे सुधार सुझाव:",
        Language.TELUGU: "✅ రెజ్యూమ్ మెరుగుదల చిట్కాలు:"
    },
    "interview_questions_label": {
        Language.ENGLISH: "Get Interview Questions",
        Language.HINDI: "साक्षात्कार प्रश्न प्राप्त करें",
        Language.TELUGU: "ఇంటర్వ్యూ ప్రశ్నలను పొందండి"
    },
    "job_title": {
        Language.ENGLISH: "Target job title:",
        Language.HINDI: "लक्ष्य नौकरी का शीर्षक:",
        Language.TELUGU: "లక్ష్య ఉద్యోగ శీర్షిక:"
    },
    "job_title_placeholder": {
        Language.ENGLISH: "e.g., Junior Software Engineer",
        Language.HINDI: "जैसे, जूनियर सॉफ्टवेयर इंजीनियर",
        Language.TELUGU: "ఉదా, జూనియర్ సాఫ్ట్‌వేర్ ఇంజనీర్"
    },
    "select_skills": {
        Language.ENGLISH: "Your relevant skills:",
        Language.HINDI: "आपके प्रासंगिक कौशल:",
        Language.TELUGU: "మీ సంబంధిత నైపుణ్యాలు:"
    },
    "generate_questions": {
        Language.ENGLISH: "Generate Interview Questions",
        Language.HINDI: "साक्षात्कार प्रश्न बनाएं",
        Language.TELUGU: "ఇంటర్వ్యూ ప్రశ్నలను ఉత్పత్తి చేయండి"
    },
    "interview_q_a": {
        Language.ENGLISH: "✅ Interview Questions & Tips:",
        Language.HINDI: "✅ साक्षात्कार प्रश्न और सुझाव:",
        Language.TELUGU: "✅ ఇంటర్వ్యూ ప్రశ్నలు & చిట్కాలు:"
    },
    "enter_job_and_skills": {
        Language.ENGLISH: "Please enter job title and select at least one skill.",
        Language.HINDI: "कृपया नौकरी का शीर्षक दर्ज करें और कम से कम एक कौशल चुनें।",
        Language.TELUGU: "దయచేసి ఉద్యోగ శీర్షికను నమోదు చేసి కనీసం ఒక నైపుణ్యాన్ని ఎంచుకోండి."
    },
    "skill_recommendations_label": {
        Language.ENGLISH: "Get Skill Recommendations",
        Language.HINDI: "कौशल सिफारिशें प्राप्त करें",
        Language.TELUGU: "నైపుణ్య సిఫారసులను పొందండి"
    },
    "current_skills_label": {
        Language.ENGLISH: "Your current skills:",
        Language.HINDI: "आपके वर्तमान कौशल:",
        Language.TELUGU: "మీ ప్రస్తుత నైపుణ్యాలు:"
    },
    "target_role": {
        Language.ENGLISH: "Target role:",
        Language.HINDI: "लक्ष्य भूमिका:",
        Language.TELUGU: "లక్ష్య పాత్ర:"
    },
    "get_recommendations": {
        Language.ENGLISH: "Get Skill Recommendations",
        Language.HINDI: "कौशल सिफारिशें प्राप्त करें",
        Language.TELUGU: "నైపుణ్య సిఫారసులను పొందండి"
    },
    "recommended_skills": {
        Language.ENGLISH: "✅ Recommended Skills to Learn:",
        Language.HINDI: "✅ सीखने के लिए अनुशंसित कौशल:",
        Language.TELUGU: "✅ నేర్చుకోవలసిన సిఫార్సు చేసిన నైపుణ్యాలు:"
    },
    "select_skills_and_role": {
        Language.ENGLISH: "Please select skills and enter target role.",
        Language.HINDI: "कृपया कौशल चुनें और लक्ष्य भूमिका दर्ज करें।",
        Language.TELUGU: "దయచేసి నైపుణ్యాలను ఎంచుకుని లక్ష్య పాత్రను నమోదు చేయండి."
    },
    "project_ideas": {
        Language.ENGLISH: "Get Project Ideas",
        Language.HINDI: "परियोजना विचार प्राप्त करें",
        Language.TELUGU: "ప్రాజెక్ట్ ఆలోచనలను పొందండి"
    },
    "experience_level": {
        Language.ENGLISH: "Your experience level:",
        Language.HINDI: "आपका अनुभव स्तर:",
        Language.TELUGU: "మీ అనుభవ స్థితి:"
    },
    "get_project_ideas": {
        Language.ENGLISH: "Get Project Ideas",
        Language.HINDI: "परियोजना विचार प्राप्त करें",
        Language.TELUGU: "ప్రాజెక్ట్ ఆలోచనలను పొందండి"
    },
    "recommended_projects": {
        Language.ENGLISH: "✅ Recommended Projects:",
        Language.HINDI: "✅ अनुशंसित परियोजनाएं:",
        Language.TELUGU: "✅ సిఫార్సు చేసిన ప్రాజెక్టులు:"
    },
    "select_skill": {
        Language.ENGLISH: "Please select at least one skill.",
        Language.HINDI: "कृपया कम से कम एक कौशल चुनें।",
        Language.TELUGU: "దయచేసి కనీసం ఒక నైపుణ్యాన్ని ఎంచుకోండి."
    },
    "ollama_config": {
        Language.ENGLISH: "Ollama Configuration",
        Language.HINDI: "ओलामा कॉन्फ़िगरेशन",
        Language.TELUGU: "ఓలామా కాన్ఫిగరేషన్"
    },
    "ollama_running": {
        Language.ENGLISH: "Make sure Ollama is running at http://localhost:11434",
        Language.HINDI: "सुनिश्चित करें कि ओलामा http://localhost:11434 पर चल रहा है",
        Language.TELUGU: "ఓలామా http://localhost:11434 నుండి నడుస్తోందని నిర్ధారించుకోండి"
    },
    "ollama_success": {
        Language.ENGLISH: "✅ Ollama is running!",
        Language.HINDI: "✅ ओलामा चल रहा है!",
        Language.TELUGU: "✅ ఓలామా నడుస్తోంది!"
    },
    "available_models": {
        Language.ENGLISH: "Available models:",
        Language.HINDI: "उपलब्ध मॉडल:",
        Language.TELUGU: "అందుబాటులో ఉన్న మోడల్‌లు:"
    },
    "model_name_label": {
        Language.ENGLISH: "Model Name:",
        Language.HINDI: "मॉडल नाम:",
        Language.TELUGU: "మోడల్ పేరు:"
    },
    "model_placeholder": {
        Language.ENGLISH: "e.g., llama3, mistral, neural-chat",
        Language.HINDI: "जैसे, llama3, mistral, neural-chat",
        Language.TELUGU: "ఉదా, llama3, mistral, neural-chat"
    },
    "test_connection": {
        Language.ENGLISH: "Test Connection",
        Language.HINDI: "कनेक्शन का परीक्षण करें",
        Language.TELUGU: "కనెక్షన్ పరీక్ష చేయండి"
    },
    "connection_successful": {
        Language.ENGLISH: "✅ Connection successful!",
        Language.HINDI: "✅ कनेक्शन सफल!",
        Language.TELUGU: "✅ కనెక్షన్ విజయవంతమైంది!"
    },
    "sample_response": {
        Language.ENGLISH: "Sample response:",
        Language.HINDI: "नमूना प्रतिक्रिया:",
        Language.TELUGU: "నమూనా ప్రతిస్పందన:"
    },
    "connection_failed": {
        Language.ENGLISH: "Failed to get response from Ollama",
        Language.HINDI: "ओलामा से प्रतिक्रिया प्राप्त करने में विफल",
        Language.TELUGU: "ఓలామా నుండి ప్రతిస్పందనను పొందటంలో విఫలమైంది"
    },
    "ollama_setup": {
        Language.ENGLISH: "How to set up Ollama:",
        Language.HINDI: "ओलामा सेटअप कैसे करें:",
        Language.TELUGU: "ఓలామాను ఎలా సెటప్ చేయాలి:"
    },
    "byok_config": {
        Language.ENGLISH: "BYOK Configuration",
        Language.HINDI: "बीवाईओके कॉन्फ़िगरेशन",
        Language.TELUGU: "బిఎయోకె కాన్ఫిగరేషన్"
    },
    "keep_api_secure": {
        Language.ENGLISH: "⚠️ Keep your API key secure. Never commit it to version control.",
        Language.HINDI: "⚠️ अपनी एपीआई कुंजी को सुरक्षित रखें। इसे कभी भी संस्करण नियंत्रण में प्रतिबद्ध न करें।",
        Language.TELUGU: "⚠️ మీ ఎపిఐ కీని సురక్షితమైనదిగా ఉంచండి. దీన్ని సంస్కరణ నియంత్రణకు ఎప్పుడూ కమిట్ చేయవద్దు."
    },
    "api_key_input": {
        Language.ENGLISH: "API Key / Token",
        Language.HINDI: "एपीआई कुंजी / टोकन",
        Language.TELUGU: "ఎపిఐ కీ / టోకన్"
    },
    "api_key_placeholder": {
        Language.ENGLISH: "Enter your API key here",
        Language.HINDI: "अपनी एपीआई कुंजी यहां दर्ज करें",
        Language.TELUGU: "మీ ఎపిఐ కీని ఇక్కడ నమోదు చేయండి"
    },
    "provider_type": {
        Language.ENGLISH: "Provider Type:",
        Language.HINDI: "प्रदाता प्रकार:",
        Language.TELUGU: "ప్రదాతా రకం:"
    },
    "api_key_configured": {
        Language.ENGLISH: "✅ API key configured (hidden for security)",
        Language.HINDI: "✅ एपीआई कुंजी कॉन्फ़िगर की गई (सुरक्षा के लिए छिपी)",
        Language.TELUGU: "✅ ఎపిఐ కీ కాన్ఫిగర్ చేయబడింది (సురక్షత కోసం దాచిన)"
    },
    "test_api_connection": {
        Language.ENGLISH: "Test API Connection",
        Language.HINDI: "एपीआई कनेक्शन का परीक्षण करें",
        Language.TELUGU: "ఎపిఐ కనెక్షన్ పరీక్ష చేయండి"
    },
    "api_testing_soon": {
        Language.ENGLISH: "API connection testing - Coming soon!",
        Language.HINDI: "एपीआई कनेक्शन परीक्षण - जल्द आ रहा है!",
        Language.TELUGU: "ఎపిఐ కనెక్షన్ పరీక్ష - త్వరలో రాబోతుంది!"
    },
    "no_api_key": {
        Language.ENGLISH: "No API key configured",
        Language.HINDI: "कोई एपीआई कुंजी कॉन्फ़िगर नहीं की गई",
        Language.TELUGU: "ఎటువంటి ఎపిఐ కీ కాన్ఫిగర్ చేయబడలేదు"
    },
    "byok_setup": {
        Language.ENGLISH: "BYOK Setup Instructions:",
        Language.HINDI: "बीवाईओके सेटअप निर्देश:",
        Language.TELUGU: "బిఎయోకె సెటప్ సూచనలు:"
    },
    "select_language": {
        Language.ENGLISH: "Select Language:",
        Language.HINDI: "भाषा चुनें:",
        Language.TELUGU: "భాషను ఎంచుకోండి:"
    },
    "select_ai_provider": {
        Language.ENGLISH: "Select AI Provider:",
        Language.HINDI: "एआई प्रदाता चुनें:",
        Language.TELUGU: "ఎఐ ప్రదాతను ఎంచుకోండి:"
    },
    "language_set": {
        Language.ENGLISH: "Language set to:",
        Language.HINDI: "भाषा सेट की गई:",
        Language.TELUGU: "భాష సెట్ చేయబడింది:"
    },
    "about": {
        Language.ENGLISH: "About",
        Language.HINDI: "परिचय",
        Language.TELUGU: "గురించి"
    },
    "version": {
        Language.ENGLISH: "Career Bridge AI v1.0",
        Language.HINDI: "कैरियर ब्रिज एआई v1.0",
        Language.TELUGU: "కెరీర్ బ్రిడ్జ్ ఎఐ v1.0"
    },
    "platform_description": {
        Language.ENGLISH: "An AI-powered career guidance platform for students",
        Language.HINDI: "छात्रों के लिए एक एआई-संचालित कैरियर मार्गदर्शन प्लेटफॉर्म",
        Language.TELUGU: "విద్యార్థుల కోసం ఎఐ-శక్తితో కూడిన కెరీర్ మార్గదర్శన ప్లాట్ఫర్మ్"
    },
    "get_api_key": {
        Language.ENGLISH: "Get an API key from your provider",
        Language.HINDI: "अपने प्रदाता से एपीआई कुंजी प्राप्त करें",
        Language.TELUGU: "మీ ప్రదాతా నుండి ఎపిఐ కీని పొందండి"
    },
    "topics_to_learn": {
        Language.ENGLISH: "Topics to Learn",
        Language.HINDI: "सीखने के लिए विषय",
        Language.TELUGU: "నేర్చుకోవలసిన విషయాలు"
    },
    "projects_to_build": {
        Language.ENGLISH: "Projects to Build",
        Language.HINDI: "बनाने के लिए परियोजनाएं",
        Language.TELUGU: "నిర్మించవలసిన ప్రాజెక్టులు"
    },
    "topics": {
        Language.ENGLISH: "Topics",
        Language.HINDI: "विषय",
        Language.TELUGU: "విషయాలు"
    },
    "no_roadmap_generated": {
        Language.ENGLISH: "No roadmap generated. Please click 'Generate Learning Roadmap' button to create your personalized roadmap.",
        Language.HINDI: "कोई रोडमैप उत्पन्न नहीं हुआ। अपना व्यक्तिगत रोडमैप बनाने के लिए 'सीखने का रोडमैप बनाएं' बटन पर क्लिक करें।",
        Language.TELUGU: "ఎటువంటి రోడ్‌మ్యాప్ ఉత్పత్తి చేయబడలేదు. మీ ఆ కేంద్రీకృత రోడ్‌మ్యాప్‌ను సృష్టించడానికి 'సిద్ధాంత రోడ్‌మ్యాప్ ఉత్పత్తి చేయండి' బటన్‌ను క్లిక్ చేయండి."
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
