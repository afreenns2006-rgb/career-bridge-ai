"""Language helpers for Career Bridge AI."""

SUPPORTED_LANGUAGES = {
    "English": {"code": "en", "instruction": "Respond in clear, beginner-friendly English."},
    "Hindi": {"code": "hi", "instruction": "Respond in Hindi using Devanagari script. Keep the tone simple and supportive."},
    "Telugu": {"code": "te", "instruction": "Respond in Telugu script. Keep the tone simple and supportive."},
}

DEFAULT_LANGUAGE = "English"

ENGLISH = {
    "navigation": "Navigation",
    "home": "Home",
    "resume_analyzer": "Resume Analyzer",
    "career_mentor": "Career Mentor",
    "scholarship_finder": "Scholarship Finder",
    "government_schemes": "Government Schemes",
    "opportunities": "Opportunities",
    "learning_roadmap": "Learning Roadmap",
    "ai_career_assistant": "AI Career Assistant",
    "deployment_diagnostics": "Deployment Diagnostics",
    "quick_links": "Quick Links",
    "language": "Response Language",
    "app_tagline": "Your Personal Career Guidance Platform",
    "documentation": "Documentation",
    "report_issue": "Report Issue",
    "contact_us": "Contact Us",
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
    "career_goals": "Career Goals",
    "your_skills": "Your Skills",
    "get_recommendations": "Get Career Recommendations",
    "get_career_recommendation": "Get Career Recommendation",
    "recommendation_spinner": "Generating career recommendations...",
    "recommendation_success": "Found career recommendations!",
    "recommendation_fallback": "Recommendation engine had an issue, so we generated a safe rule-based recommendation.",
    "recommendation_prompt": "Add your skills and click Get Career Recommendation to see suggestions.",
    "match_score": "Match Score",
    "growth_potential": "Growth Potential",
    "salary_range": "Salary Range",
    "required_skills": "Required Skills",
    "matching_skills": "Matching Skills",
    "suggested_next_steps": "Suggested Next Steps",
    "rule_based_fallback": "Rule-based fallback",
    "learn_more": "Learn More",
    "not_available": "Not available",
    "ats_score": "ATS Score",
    "skills_found": "Skills Found",
    "needs_improvement": "Needs Improvement",
    "good": "Good",
    "complete": "Complete",
    "missing": "Missing",
    "interests": "Interests",
    "selected_response_language": "Selected response language",
    "ai_provider_settings": "AI Provider Settings",
    "your_question": "Your Question",
    "ask_career_related": "Ask anything career-related",
    "career_question_placeholder": "Example: I know Python and SQL. How can I become a data analyst?",
    "generate_ai_guidance": "Generate AI Guidance",
    "generating_career_guidance": "Generating career guidance...",
    "ai_guidance": "AI Guidance",
    "no_major_gap": "No major gap detected",
    "recommended_career_path": "Recommended Career Path",
    "core_role_skills": "Core role skills",
    "home_title": "Career Bridge AI",
    "home_subtitle": "AI-powered career guidance for students, fresh graduates, and job seekers.",
    "home_intro": "Choose a tool from the sidebar to analyze resumes, explore career paths, find opportunities, or ask the AI Career Assistant.",
    "main_features": "Main Features",
}

UI_TRANSLATIONS = {
    "English": ENGLISH,
    "Hindi": {
        **ENGLISH,
        "navigation": "\u0928\u0947\u0935\u093f\u0917\u0947\u0936\u0928",
        "home": "\u0939\u094b\u092e",
        "resume_analyzer": "\u0930\u093f\u091c\u094d\u092f\u0942\u092e\u0947 \u0935\u093f\u0936\u094d\u0932\u0947\u0937\u0915",
        "career_mentor": "\u0915\u0930\u093f\u092f\u0930 \u092e\u0947\u0902\u091f\u0930",
        "language": "\u092a\u094d\u0930\u0924\u093f\u0915\u094d\u0930\u093f\u092f\u093e \u092d\u093e\u0937\u093e",
        "resume_header": "\u0930\u093f\u091c\u094d\u092f\u0942\u092e\u0947 \u0935\u093f\u0936\u094d\u0932\u0947\u0937\u0915",
        "career_header": "\u0915\u0930\u093f\u092f\u0930 \u092e\u0947\u0902\u091f\u0930",
    },
    "Telugu": {
        **ENGLISH,
        "navigation": "\u0c28\u0c3e\u0c35\u0c3f\u0c17\u0c47\u0c37\u0c28\u0c4d",
        "home": "\u0c39\u0c4b\u0c2e\u0c4d",
        "resume_analyzer": "\u0c30\u0c46\u0c1c\u0c4d\u0c2f\u0c42\u0c2e\u0c47 \u0c35\u0c3f\u0c36\u0c4d\u0c32\u0c47\u0c37\u0c23",
        "career_mentor": "\u0c15\u0c46\u0c30\u0c40\u0c30\u0c4d \u0c2e\u0c46\u0c02\u0c1f\u0c30\u0c4d",
        "language": "\u0c38\u0c4d\u0c2a\u0c02\u0c26\u0c28 \u0c2d\u0c3e\u0c37",
        "resume_header": "\u0c30\u0c46\u0c1c\u0c4d\u0c2f\u0c42\u0c2e\u0c47 \u0c35\u0c3f\u0c36\u0c4d\u0c32\u0c47\u0c37\u0c23",
        "career_header": "\u0c15\u0c46\u0c30\u0c40\u0c30\u0c4d \u0c2e\u0c46\u0c02\u0c1f\u0c30\u0c4d",
    },
}

TRANSLATIONS = UI_TRANSLATIONS


def get_language_names() -> list[str]:
    return list(SUPPORTED_LANGUAGES.keys())


def normalize_language(language: str | None) -> str:
    return language if language in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE


def get_language_instruction(language: str) -> str:
    return SUPPORTED_LANGUAGES[normalize_language(language)]["instruction"]


def get_language_code(language: str) -> str:
    return SUPPORTED_LANGUAGES[normalize_language(language)]["code"]


def translate(key: str, language: str | None = None) -> str:
    selected = normalize_language(language)
    return UI_TRANSLATIONS.get(selected, {}).get(key) or UI_TRANSLATIONS["English"].get(key, key)


def build_rule_based_response(question: str, language: str) -> str:
    language = normalize_language(language)
    if language == "Hindi":
        return f"""
### \u0915\u0930\u093f\u092f\u0930 \u0930\u094b\u0921\u092e\u0948\u092a
1. \u0905\u092a\u0928\u093e \u0932\u0915\u094d\u0937\u094d\u092f \u0930\u094b\u0932 \u091a\u0941\u0928\u0947\u0902 \u0914\u0930 \u091c\u0930\u0942\u0930\u0940 \u0915\u094c\u0936\u0932 \u0932\u093f\u0916\u0947\u0902.
2. \u092c\u0941\u0928\u093f\u092f\u093e\u0926\u0940 \u0915\u094c\u0936\u0932 \u0938\u0940\u0916\u0947\u0902 \u0914\u0930 \u092a\u094d\u0930\u094b\u091c\u0947\u0915\u094d\u091f \u092c\u0928\u093e\u090f\u0902.

### \u0938\u094d\u0915\u093f\u0932 \u0938\u0941\u091d\u093e\u0935
- Python, SQL, communication \u0914\u0930 problem solving \u092e\u091c\u092c\u0942\u0924 \u0915\u0930\u0947\u0902.

**\u0906\u092a\u0915\u093e \u0938\u0935\u093e\u0932:** {question}
"""
    if language == "Telugu":
        return f"""
### \u0c15\u0c46\u0c30\u0c40\u0c30\u0c4d \u0c30\u0c4b\u0c21\u0c4d\u0c2e\u0c4d\u0c2f\u0c3e\u0c2a\u0c4d
1. \u0c2e\u0c40 \u0c32\u0c15\u0c4d\u0c37\u0c4d\u0c2f \u0c2a\u0c3e\u0c24\u0c4d\u0c30\u0c28\u0c41 \u0c0e\u0c02\u0c1a\u0c41\u0c15\u0c4b\u0c02\u0c21\u0c3f.
2. \u0c2a\u0c4d\u0c30\u0c3e\u0c25\u0c2e\u0c3f\u0c15 \u0c28\u0c48\u0c2a\u0c41\u0c23\u0c4d\u0c2f\u0c3e\u0c32\u0c41 \u0c28\u0c47\u0c30\u0c4d\u0c1a\u0c41\u0c15\u0c41\u0c28\u0c3f \u0c2a\u0c4d\u0c30\u0c3e\u0c1c\u0c46\u0c15\u0c4d\u0c1f\u0c4d\u0c32\u0c41 \u0c1a\u0c47\u0c2f\u0c02\u0c21\u0c3f.

### \u0c38\u0c4d\u0c15\u0c3f\u0c32\u0c4d \u0c38\u0c42\u0c1a\u0c28\u0c32\u0c41
- Python, SQL, communication, problem solving \u0c28\u0c48\u0c2a\u0c41\u0c23\u0c4d\u0c2f\u0c3e\u0c32\u0c28\u0c41 \u0c2c\u0c32\u0c2a\u0c30\u0c1a\u0c02\u0c21\u0c3f.

**\u0c2e\u0c40 \u0c2a\u0c4d\u0c30\u0c36\u0c4d\u0c28:** {question}
"""
    return f"""
### Career Roadmap
1. Pick one target role and list the skills it requires.
2. Spend 30 days on foundations, then build small proof-of-work projects.
3. Update your resume and LinkedIn/GitHub profile every week.

### Resume Improvement Tips
- Add numbers to achievements wherever possible.
- For every project, explain the problem, technology used, and result.

### Interview Questions
- Walk me through your strongest project.
- What problem did you solve and why did you choose that approach?

### Skill and Project Suggestions
- Strengthen Python, SQL, communication, and problem solving.
- Build one portfolio project, one data analysis project, and one deployed application.

**Your question:** {question}
"""
