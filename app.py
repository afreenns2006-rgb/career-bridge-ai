"""
Career Bridge AI - Main Streamlit Application

A comprehensive AI-powered student career guidance platform providing
resume analysis, career recommendations, scholarship finder, government
scheme recommendations, opportunity discovery, and learning roadmaps.

Features:
- AI-powered Career Assistant (Ollama + BYOK support)
- Multilingual support (English, Hindi, Telugu)
- Resume analysis with ATS scoring
- Career recommendations
- Scholarship finder
- Government scheme recommender
- Opportunity discovery
- Personalized learning roadmap
"""

import logging
import os
<<<<<<< HEAD
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from config import STREAMLIT_PAGE_TITLE, STREAMLIT_PAGE_ICON, STREAMLIT_LAYOUT, ensure_directories
=======
from dotenv import load_dotenv

from config import (
    STREAMLIT_PAGE_TITLE,
    STREAMLIT_PAGE_ICON,
    STREAMLIT_LAYOUT,
    ensure_directories,
    AI_PROVIDER,
    OLLAMA_MODEL,
    BYOK_API_KEY,
    DEFAULT_LANGUAGE,
    ENABLE_MULTILINGUAL
)
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
from database import get_db_manager
from career_engine import CareerRecommendationEngine
from opportunity_engine import OpportunityEngine, DEFAULT_OPPORTUNITIES
from resume_parser import ResumeParser
from roadmap_engine import RoadmapGenerator
<<<<<<< HEAD
from scholarship_engine import ScholarshipRecommendationEngine, DEFAULT_SCHOLARSHIPS
from scheme_engine import GovernmentSchemeEngine, DEFAULT_SCHEMES
from services.ai_provider import (
    DEFAULT_BYOK_ENDPOINT,
    DEFAULT_BYOK_MODEL,
    DEFAULT_OLLAMA_MODEL,
    OLLAMA_GENERATE_URL,
    AIProviderConfig,
    generate_ai_response,
)
from services.language import get_language_names, normalize_language, translate
=======
from services.language import Language, get_text, get_supported_languages
from services.ai_provider import create_ai_service, OllamaProvider

# Load environment variables
load_dotenv()
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

if Path(".env").exists():
    load_dotenv()


def get_runtime_setting(name: str, default: str = "") -> str:
    """Read Streamlit secrets first, then environment variables, without failing on deployment."""
    try:
        if name in st.secrets:
            return str(st.secrets[name])
    except Exception:
        pass
    return os.getenv(name, default)



# Configure Streamlit page
st.set_page_config(
    page_title=STREAMLIT_PAGE_TITLE,
    page_icon=STREAMLIT_PAGE_ICON,
    layout=STREAMLIT_LAYOUT,
    initial_sidebar_state="expanded",
)


def initialize_session_state() -> None:
    """
    Initialize Streamlit session state variables.
<<<<<<< HEAD

    TODO: Implement session state initialization for:
=======
    
    Initializes:
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        - User profile
        - Uploaded files
        - Recommendations
        - Learning plans
        - Language settings
        - AI provider settings
    """
    if "user_profile" not in st.session_state:
        st.session_state.user_profile = {
            "name": "",
            "email": "",
            "education_level": "",
            "experience_years": 0,
            "skills": [],
            "state": "",
            "annual_income": 0,
        }

    if "resume_data" not in st.session_state:
        st.session_state.resume_data = None

    if "career_recommendations_data" not in st.session_state:
        st.session_state.career_recommendations_data = []

    if "scholarship_recommendations" not in st.session_state:
        st.session_state.scholarship_recommendations = []

    if "scheme_recommendations" not in st.session_state:
        st.session_state.scheme_recommendations = []

    if "learning_plan" not in st.session_state:
        st.session_state.learning_plan = None
    
    # Language and AI settings
    if "language" not in st.session_state:
        st.session_state.language = Language(DEFAULT_LANGUAGE)
    
    if "ai_provider" not in st.session_state:
        st.session_state.ai_provider = AI_PROVIDER
    
    if "ai_service" not in st.session_state:
        st.session_state.ai_service = None
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "ai_assistant_response" not in st.session_state:
        st.session_state.ai_assistant_response = ""

    if "ai_assistant_warning" not in st.session_state:
        st.session_state.ai_assistant_warning = False

    if "language" not in st.session_state:
        st.session_state.language = normalize_language(
            st.session_state.get("selected_language") or get_runtime_setting("DEFAULT_LANGUAGE", "English")
        )
    else:
        st.session_state.language = normalize_language(st.session_state.language)

    # Keep the older key in sync for existing AI/language code paths.
    st.session_state.selected_language = st.session_state.language

    if "language_selector" not in st.session_state:
        st.session_state.language_selector = st.session_state.language


def render_sidebar() -> str:
    """
<<<<<<< HEAD
    Render sidebar navigation.

    Returns:
        Selected page name.

    TODO: Implement sidebar with page navigation links.
=======
    Render sidebar navigation with language selector and AI settings.
    
    Returns:
        Selected page name.
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    """
    st.sidebar.title(get_text("app_title", st.session_state.language))
    st.sidebar.write(get_text("tagline", st.session_state.language))
    st.sidebar.divider()
<<<<<<< HEAD

    page = st.sidebar.radio(
        "Navigation",
        options=[
            "Home",
            "Resume Analyzer",
            "Career Mentor",
            "Scholarship Finder",
            "Government Schemes",
            "Opportunities",
            "Learning Roadmap",
            "AI Career Assistant",
=======
    
    # Language selector
    if ENABLE_MULTILINGUAL:
        st.sidebar.markdown("### " + get_text("language", st.session_state.language))
        language_options = get_supported_languages()
        selected_lang = st.sidebar.selectbox(
            get_text("language", st.session_state.language),
            options=list(language_options.keys()),
            index=list(language_options.values()).index(st.session_state.language),
            label_visibility="collapsed"
        )
        st.session_state.language = language_options[selected_lang]
    
    st.sidebar.divider()
    
    # Navigation menu
    page = st.sidebar.radio(
        "Navigation",
        options=[
            get_text("home", st.session_state.language),
            get_text("resume_analyzer", st.session_state.language),
            get_text("career_mentor", st.session_state.language),
            get_text("ai_assistant", st.session_state.language),
            get_text("scholarship_finder", st.session_state.language),
            get_text("government_schemes", st.session_state.language),
            get_text("opportunities", st.session_state.language),
            get_text("learning_roadmap", st.session_state.language),
            get_text("settings", st.session_state.language)
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        ],
        index=0,
    )

    render_language_selector()

    st.sidebar.divider()
    st.sidebar.markdown("### Quick Links")
    st.sidebar.markdown("[Documentation](https://github.com/CareerBridgeAI)")
    st.sidebar.markdown("[Report Issue](https://github.com/CareerBridgeAI/issues)")
    st.sidebar.markdown("[Contact Us](mailto:support@careerbridgeai.com)")

    return page


def render_language_selector() -> None:
    """Render the language selector in a deployment-safe way."""
    st.sidebar.divider()
    language_options = get_language_names()

    try:
        if "selected_language" in st.session_state:
            if st.session_state.selected_language not in language_options:
                del st.session_state["selected_language"]
            else:
                st.sidebar.selectbox(
                    "🌐 Response Language",
                    options=language_options,
                    key="selected_language",
                    help="AI Career Assistant responses will use this language.",
                )
                return

        default_language = normalize_language(get_runtime_setting("DEFAULT_LANGUAGE", "English"))
        st.sidebar.selectbox(
            "🌐 Response Language",
            options=language_options,
            index=language_options.index(default_language),
            key="selected_language",
            help="AI Career Assistant responses will use this language.",
        )
    except Exception as exc:
        logger.warning("Language selector failed to render: %s", exc)
        st.sidebar.warning("Language selector could not load. Using English for now.")


def render_home_page() -> None:
    """
    Render home/landing page.

    Displays welcome message and feature overview.

    TODO: Implement home page with:
        - Welcome message
        - Feature descriptions
        - Getting started guide
        - Quick stats
    """
<<<<<<< HEAD
    st.title("🎓 Career Bridge AI")
    st.write("Welcome to Career Bridge AI - Your Personal Career Guidance Platform")

    st.markdown("""
    ## Bridging Students to Opportunities
=======
    st.title(get_text("app_title", st.session_state.language))
    st.write(get_text("welcome_message", st.session_state.language))
    
    st.markdown(f"""
    ## {get_text("bridging_students", st.session_state.language)}
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    
    {get_text("career_guidance", st.session_state.language)}
    """)

    # Feature cards
    col1, col2, col3 = st.columns(3)

    with col1:
<<<<<<< HEAD
        st.info(
            "📄 **Resume Analyzer**\nGet AI-powered analysis of your resume with ATS scoring and improvement suggestions."
        )

    with col2:
        st.success(
            "💼 **Career Recommendations**\nDiscover career paths that match your skills and experience with detailed guidance."
        )

    with col3:
        st.warning("🎓 **Scholarship Finder**\nFind and apply for scholarships matching your eligibility criteria.")

=======
        st.info(get_text("resume_analyzer_desc", st.session_state.language))
    
    with col2:
        st.success(get_text("career_recommendations_desc", st.session_state.language))
    
    with col3:
        st.warning(get_text("scholarship_finder_desc", st.session_state.language))
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    st.markdown("---")

    col4, col5, col6 = st.columns(3)

    with col4:
<<<<<<< HEAD
        st.info("🏛️ **Government Schemes**\nAccess information about government schemes and assistance programs.")

    with col5:
        st.success("🚀 **Opportunities**\nExplore internships, competitions, and career-building opportunities.")

    with col6:
        st.warning("🗺️ **Learning Roadmap**\nCreate personalized learning paths to bridge your skill gaps.")

=======
        st.info(get_text("government_schemes_desc", st.session_state.language))
    
    with col5:
        st.success(get_text("opportunities_desc", st.session_state.language))
    
    with col6:
        st.warning(get_text("learning_roadmap_desc", st.session_state.language))
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    st.markdown("---")

    # Quick statistics
    st.markdown(f"## {get_text('platform_statistics', st.session_state.language)}")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
<<<<<<< HEAD
        st.metric("Active Users", "10,000+", "+15%")

    with col2:
        st.metric("Opportunities", "5,000+", "+20%")

    with col3:
        st.metric("Scholarships", "1,500+", "+10%")

    with col4:
        st.metric("Success Rate", "85%", "+5%")

=======
        st.metric(get_text("active_users", st.session_state.language), "10,000+", "+15%")
    
    with col2:
        st.metric(get_text("total_opportunities", st.session_state.language), "5,000+", "+20%")
    
    with col3:
        st.metric(get_text("total_scholarships", st.session_state.language), "1,500+", "+10%")
    
    with col4:
        st.metric(get_text("success_rate", st.session_state.language), "85%", "+5%")
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    st.markdown("---")

    # Getting started
    st.markdown(f"## {get_text('getting_started', st.session_state.language)}")
    st.markdown(f"""
    1. **{get_text('home', st.session_state.language)}** - {get_text('upload_resume', st.session_state.language)}
    2. **{get_text('career_mentor', st.session_state.language)}** - {get_text('personalized_recommendations', st.session_state.language)}
    3. **{get_text('scholarship_finder', st.session_state.language)}** - {get_text('discover_scholarships', st.session_state.language)}
    4. **{get_text('opportunities', st.session_state.language)}** - {get_text('explore_opportunities', st.session_state.language)}
    5. **{get_text('learning_roadmap', st.session_state.language)}** - {get_text('create_learning_roadmap', st.session_state.language)}
    """)


def render_resume_analyzer() -> None:
    """
    Render Resume Analyzer page.

    Allows users to upload and analyze their resume.

    TODO: Implement resume analysis page with:
        - File upload functionality
        - Text extraction display
        - Skill extraction results
        - ATS score display
        - Improvement suggestions
    """
<<<<<<< HEAD
    st.header("📄 Resume Analyzer")
    st.write("Upload your resume for analysis")

    # File upload
    uploaded_file = st.file_uploader("Upload your resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

=======
    st.header(get_text("resume_analyzer", st.session_state.language))
    st.write(get_text("upload_resume", st.session_state.language))
    
    # File upload
    uploaded_file = st.file_uploader(
        get_text("upload_file", st.session_state.language),
        type=["pdf", "docx", "txt"]
    )
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    if uploaded_file is not None:
        # Parse directly from the Streamlit upload; this works on Streamlit Cloud.
        parser = ResumeParser.from_upload(uploaded_file)

        if not parser.validate_resume():
<<<<<<< HEAD
            st.error("Could not extract text from the resume. Please upload a readable PDF/DOCX.")
=======
            st.error(get_text("invalid_resume", st.session_state.language))
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
            return

        # Extract information
        with st.spinner(get_text("analyzing_resume", st.session_state.language)):
            text = parser.extract_text()
            skills = parser.extract_skills()
            education = parser.extract_education()
            experience = parser.extract_experience()
            ats_score = parser.calculate_ats_score()

        st.session_state.resume_data = {
            "text": text,
            "skills": skills,
            "education": education,
            "experience": experience,
            "ats_score": ats_score,
        }

        # Display results
<<<<<<< HEAD
        st.success("✅ Resume analyzed successfully!")

=======
        st.success(get_text("resume_analyzed", st.session_state.language))
        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        col1, col2, col3 = st.columns(3)

        with col1:
<<<<<<< HEAD
            st.metric("ATS Score", f"{ats_score:.1f}/100", delta="Good" if ats_score > 70 else "Needs Improvement")

        with col2:
            st.metric("Skills Found", len(skills), delta=f"+{len(skills)}")

        with col3:
            st.metric("Education", len(education), delta="Complete" if education else "Missing")

=======
            st.metric(
                get_text("ats_score", st.session_state.language),
                f"{ats_score:.1f}/100",
                delta="Good" if ats_score > 70 else "Needs Improvement"
            )
        
        with col2:
            st.metric(
                get_text("skills_found", st.session_state.language),
                len(skills),
                delta=f"+{len(skills)}"
            )
        
        with col3:
            st.metric(
                get_text("education_label", st.session_state.language),
                len(education),
                delta="Complete" if education else "Missing"
            )
        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        st.markdown("---")

        # Skills section
        st.markdown(f"## {get_text('extracted_skills', st.session_state.language)}")
        if skills:
            cols = st.columns(4)
            for idx, skill in enumerate(skills):
                with cols[idx % 4]:
                    st.label_option_text(skill)
        else:
<<<<<<< HEAD
            st.info("No skills detected. Please ensure your resume contains your skills.")

=======
            st.info(get_text("no_skills_detected", st.session_state.language))
        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        st.markdown("---")

        # Education section
        st.markdown(f"## {get_text('education_label', st.session_state.language)}")
        if education:
            for edu in education:
                st.write(f"📚 {edu.get('type', 'Degree')}")
        else:
<<<<<<< HEAD
            st.info("No education information found.")

=======
            st.info(get_text("no_education_found", st.session_state.language))
        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        st.markdown("---")

        # Experience section
        st.markdown(f"## {get_text('work_experience', st.session_state.language)}")
        if experience:
            for exp in experience:
                st.write(f"💼 {exp.get('title', 'Position')}")
        else:
<<<<<<< HEAD
            st.info("No work experience found.")

=======
            st.info(get_text("no_experience_found", st.session_state.language))
        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        st.markdown("---")

        # Improvement suggestions
        st.markdown(f"## {get_text('improvement_suggestions', st.session_state.language)}")
        suggestions = []

        if ats_score < 50:
            suggestions.append("✓ Add more keywords from your industry")
        if len(skills) < 5:
            suggestions.append("✓ Include more specific technical skills")
        if not education:
            suggestions.append("✓ Add your educational background")
        if not experience:
            suggestions.append("✓ Include your work experience")

        if suggestions:
            for suggestion in suggestions:
                st.write(suggestion)
        else:
            st.success(get_text("resume_looks_good", st.session_state.language))


def render_career_mentor() -> None:
    """
    Render Career Mentor page.

    Provides career recommendations based on user profile.

    TODO: Implement career mentor page with:
        - User profile form
        - Career recommendations
        - Skill gap analysis
        - Career details display
        - Similar careers
    """
<<<<<<< HEAD
    st.header("💼 Career Mentor")
    st.write("Get personalized career recommendations")

=======
    st.header(f"💼 {get_text('career_mentor', st.session_state.language)}")
    st.write(get_text("personalized_recommendations", st.session_state.language))
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    # User profile form
    st.markdown(f"### {get_text('your_profile', st.session_state.language)}")
    col1, col2 = st.columns(2)

    with col1:
<<<<<<< HEAD
        experience_years = st.slider("Years of Experience", 0, 50, 2)
        education_level = st.selectbox("Education Level", ["10th", "12th", "UG", "PG", "Diploma"])

=======
        experience_years = st.slider(get_text("years_of_experience", st.session_state.language), 0, 50, 2)
        education_level = st.selectbox(
            get_text("education_level", st.session_state.language),
            ["10th", "12th", "UG", "PG", "Diploma"]
        )
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    with col2:
        st.markdown("")
        st.session_state.user_profile["education_level"] = education_level
        st.session_state.user_profile["experience_years"] = experience_years

    # Get skills from resume or manual input
    skills_input = st.multiselect(
        get_text("your_skills", st.session_state.language),
        options=[
            "python",
            "java",
            "javascript",
            "sql",
            "machine learning",
            "data analysis",
            "web development",
            "cloud computing",
            "communication",
            "leadership",
            "problem solving",
        ],
        default=st.session_state.resume_data.get("skills", []) if st.session_state.resume_data else [],
    )
<<<<<<< HEAD
    st.session_state.user_profile["skills"] = skills_input

    if st.button("Get Career Recommendations", key="career_recommendations_widget"):
        with st.spinner("Generating career recommendations..."):
=======
    
    if st.button(get_text("get_career_recommendations", st.session_state.language), key="career_recommendations_widget"):
        with st.spinner(get_text("loading", st.session_state.language)):
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
            career_engine = CareerRecommendationEngine()
            recommendations = career_engine.recommend_careers(
                user_skills=skills_input, education=education_level, experience_years=experience_years
            )

        st.session_state.career_recommendations_data = recommendations

        if recommendations:
            st.success(f"✅ {get_text('career_recommendations_found', st.session_state.language).format(count=len(recommendations))}")
            st.markdown("---")

            # Display recommendations
            for idx, rec in enumerate(recommendations, 1):
                with st.container():
                    col1, col2 = st.columns([3, 1])

                    with col1:
                        st.markdown(f"### {idx}. {rec['career_name']}")
<<<<<<< HEAD
                        st.write(f"**Match Score:** {rec['match_score']}%")
                        st.write(f"**Salary Range:** {rec['salary_range']}")
                        st.write(f"**Growth Potential:** {rec['growth_potential']}")

=======
                        st.write(f"**{get_text('match_score', st.session_state.language)}:** {rec['match_score']}%")
                        st.write(f"**{get_text('salary_range', st.session_state.language)}:** {rec['salary_range']}")
                        st.write(f"**{get_text('growth_potential', st.session_state.language)}:** {rec['growth_potential']}")
                        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
                        # Matching skills
                        matching = rec.get("matching_skills", [])
                        if matching:
<<<<<<< HEAD
                            st.markdown("**Matching Skills:** " + ", ".join(matching))

=======
                            st.markdown(f"**{get_text('matching_skills', st.session_state.language)}:** " + ", ".join(matching))
                        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
                        # Missing skills
                        missing = rec.get("missing_skills", [])
                        if missing:
<<<<<<< HEAD
                            st.markdown("**Skills to Learn:** " + ", ".join(missing))

=======
                            st.markdown(f"**{get_text('skills_to_learn', st.session_state.language)}:** " + ", ".join(missing))
                    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
                    with col2:
                        if st.button(get_text("learn_more", st.session_state.language), key=f"career_{idx}"):
                            st.info(f"Career: {rec['career_name']}\n\nSkills: {', '.join(rec['required_skills'])}")

                    st.divider()
        else:
            st.info(get_text("no_recommendations", st.session_state.language))


def render_scholarship_finder() -> None:
    """
    Render Scholarship Finder page.

    Helps find suitable scholarships.

    TODO: Implement scholarship finder page with:
        - Eligibility form
        - Scholarship search/filter
        - Eligibility status
        - Application timeline
        - Link to applications
    """
<<<<<<< HEAD
    st.header("🎓 Scholarship Finder")
    st.write("Discover scholarship opportunities")

=======
    st.header(f"🎓 {get_text('scholarship_finder', st.session_state.language)}")
    st.write(get_text("discover_scholarships", st.session_state.language))
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    # Eligibility form
    st.markdown(f"### {get_text('your_details', st.session_state.language)}")
    col1, col2 = st.columns(2)

    with col1:
<<<<<<< HEAD
        education_level = st.selectbox("Education Level", ["10th", "12th", "UG", "PG"], key="scholarship_education")
        state = st.text_input("State", value=st.session_state.user_profile.get("state", ""))

    with col2:
        annual_income = st.number_input(
            "Annual Family Income (₹)", min_value=0, value=st.session_state.user_profile.get("annual_income", 0)
        )
        gpa = st.number_input("GPA (if available)", min_value=0.0, max_value=4.0, value=3.5)

    st.markdown("---")

    if st.button("Find Scholarships", key="find_scholarships"):
        try:
            with st.spinner("Searching for scholarships..."):
                scholarship_engine = ScholarshipRecommendationEngine()
                recommendations = scholarship_engine.recommend_scholarships(
                    education_level=education_level, state=state, annual_income=annual_income, gpa=gpa
                )
        except Exception as exc:
            logger.exception("Scholarship finder failed, using fallback dataset: %s", exc)
            st.warning("Scholarship service unavailable. Showing fallback results.")
            recommendations = fallback_scholarships(education_level, annual_income)

=======
        education_level = st.selectbox(
            get_text("education_level", st.session_state.language),
            ["10th", "12th", "UG", "PG"],
            key="scholarship_education"
        )
        state = st.text_input(
            get_text("state", st.session_state.language),
            value=st.session_state.user_profile.get("state", "")
        )
    
    with col2:
        annual_income = st.number_input(
            get_text("annual_income", st.session_state.language),
            min_value=0,
            value=st.session_state.user_profile.get("annual_income", 0)
        )
        gpa = st.number_input(
            get_text("gpa", st.session_state.language),
            min_value=0.0,
            max_value=4.0,
            value=3.5
        )
    
    st.markdown("---")
    
    if st.button(get_text("find_scholarships", st.session_state.language), key="find_scholarships"):
        with st.spinner(get_text("loading", st.session_state.language)):
            scholarship_engine = ScholarshipRecommendationEngine()
            recommendations = scholarship_engine.recommend_scholarships(
                education_level=education_level,
                state=state,
                annual_income=annual_income,
                gpa=gpa
            )
        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        st.session_state.scholarship_recommendations = recommendations

        if recommendations:
            st.success(f"✅ {get_text('scholarships_found', st.session_state.language).format(count=len(recommendations))}")
            st.markdown("---")

            # Display scholarships
            for idx, scholarship in enumerate(recommendations, 1):
                with st.container():
                    col1, col2 = st.columns([3, 1])

                    with col1:
                        st.markdown(f"### {idx}. {scholarship['scholarship_name']}")
<<<<<<< HEAD
                        st.write(f"**Award Amount:** ₹{scholarship['award_amount']:,}")
                        st.write(f"**Eligibility:** {scholarship['eligibility']}")
                        st.write(f"**Deadline:** {scholarship['deadline']}")
                        st.write(f"**Match Score:** {scholarship['match_score']}%")

                    with col2:
                        if st.button("Apply Now", key=f"apply_{idx}"):
                            st.success(f"Redirecting to {scholarship['scholarship_name']} application...")

=======
                        st.write(f"**{get_text('award_amount', st.session_state.language)}:** ₹{scholarship['award_amount']:,}")
                        st.write(f"**{get_text('eligibility', st.session_state.language)}:** {scholarship['eligibility']}")
                        st.write(f"**{get_text('deadline', st.session_state.language)}:** {scholarship['deadline']}")
                        st.write(f"**{get_text('match_score', st.session_state.language)}:** {scholarship['match_score']}%")
                    
                    with col2:
                        if st.button(get_text("apply_now", st.session_state.language), key=f"apply_{idx}"):
                            st.success(f"{get_text('redirecting', st.session_state.language)}")
                    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
                    st.divider()
        else:
            st.info(get_text("no_scholarships", st.session_state.language))


def render_scheme_recommender() -> None:
    """
    Render Government Scheme Recommender page.

    Recommends relevant government schemes.

    TODO: Implement scheme recommender page with:
        - Eligibility criteria form
        - Scheme recommendations
        - Eligibility details
        - Application process
        - Required documents
    """
<<<<<<< HEAD
    st.header("🏛️ Government Scheme Recommender")
    st.write("Find relevant government schemes")

=======
    st.header(f"🏛️ {get_text('government_schemes', st.session_state.language)}")
    st.write(get_text("government_scheme_desc", st.session_state.language))
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    # Eligibility form
    st.markdown(f"### {get_text('your_details', st.session_state.language)}")
    col1, col2 = st.columns(2)

    with col1:
<<<<<<< HEAD
        state = st.text_input("State", value=st.session_state.user_profile.get("state", ""))
        education_level = st.selectbox("Education Level", ["10th", "12th", "UG", "PG"], key="scheme_education")

=======
        state = st.text_input(
            get_text("state", st.session_state.language),
            value=st.session_state.user_profile.get("state", "")
        )
        education_level = st.selectbox(
            get_text("education_level", st.session_state.language),
            ["10th", "12th", "UG", "PG"],
            key="scheme_education"
        )
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    with col2:
        age = st.number_input(
            get_text("age", st.session_state.language),
            min_value=1,
            max_value=100,
            value=20
        )
        annual_income = st.number_input(
            get_text("annual_income", st.session_state.language),
            min_value=0,
            value=st.session_state.user_profile.get("annual_income", 0),
            key="scheme_income",
        )

    category = st.selectbox(
<<<<<<< HEAD
        "Social Category", ["General", "OBC", "SC", "ST"], help="Select your social category for eligibility"
=======
        get_text("social_category", st.session_state.language),
        ["General", "OBC", "SC", "ST"],
        help=get_text("select_category", st.session_state.language)
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    )

    st.markdown("---")
<<<<<<< HEAD

    if st.button("Get Scheme Recommendations", key="get_schemes"):
        try:
            with st.spinner("Finding government schemes..."):
                scheme_engine = GovernmentSchemeEngine()
                recommendations = scheme_engine.recommend_schemes(
                    state=state, education_level=education_level, annual_income=annual_income, age=age, category=category
                )
        except Exception as exc:
            logger.exception("Government schemes failed, using fallback dataset: %s", exc)
            st.warning("Government scheme service unavailable. Showing fallback results.")
            recommendations = fallback_schemes(annual_income, age)

=======
    
    if st.button(get_text("get_scheme_recommendations", st.session_state.language), key="get_schemes"):
        with st.spinner(get_text("loading", st.session_state.language)):
            scheme_engine = GovernmentSchemeEngine()
            recommendations = scheme_engine.recommend_schemes(
                state=state,
                education_level=education_level,
                annual_income=annual_income,
                age=age,
                category=category
            )
        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        st.session_state.scheme_recommendations = recommendations

        if recommendations:
            st.success(f"✅ {get_text('schemes_found', st.session_state.language).format(count=len(recommendations))}")
            st.markdown("---")

            # Display schemes
            for idx, scheme in enumerate(recommendations, 1):
                with st.expander(f"**{idx}. {scheme['scheme_name']}**"):
                    col1, col2 = st.columns(2)

                    with col1:
<<<<<<< HEAD
                        st.write(f"**Type:** {scheme['scheme_type']}")
                        st.write(f"**Benefit:** {scheme['benefit']}")
                        st.write(f"**Eligibility:** {scheme['eligibility']}")

                    with col2:
                        st.write(f"**Deadline:** {scheme['deadline']}")
                        st.write(f"**Max Income:** ₹{scheme['max_income']:,}")
                        st.write(f"**Age Limit:** {scheme['age_limit']} years")

=======
                        st.write(f"**{get_text('scheme_type', st.session_state.language)}:** {scheme['scheme_type']}")
                        st.write(f"**{get_text('benefit', st.session_state.language)}:** {scheme['benefit']}")
                        st.write(f"**{get_text('eligibility', st.session_state.language)}:** {scheme['eligibility']}")
                    
                    with col2:
                        st.write(f"**{get_text('deadline', st.session_state.language)}:** {scheme['deadline']}")
                        st.write(f"**{get_text('max_income', st.session_state.language)}:** ₹{scheme['max_income']:,}")
                        st.write(f"**{get_text('age_limit', st.session_state.language)}:** {scheme['age_limit']} years")
                    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
                    # Application process
                    st.markdown(f"**{get_text('application_process', st.session_state.language)}:**")
                    st.markdown("""
                    1. Verify eligibility criteria
                    2. Gather required documents
                    3. Complete application form
                    4. Submit to government office
                    5. Track status
                    """)

                    # Required documents
                    st.markdown(f"**{get_text('required_documents', st.session_state.language)}:**")
                    documents = [
                        "Aadhar Card",
                        "Educational Certificate",
                        "Income Certificate",
                        "Bank Passbook",
                        "Address Proof",
                    ]
                    for doc in documents:
                        st.write(f"• {doc}")
        else:
            st.info(get_text("no_schemes", st.session_state.language))


def render_opportunity_dashboard() -> None:
    """
    Render Opportunity Dashboard page.

    Shows available opportunities matching user profile.

    TODO: Implement opportunity dashboard with:
        - Opportunity search
        - Filter options
        - Opportunity cards
        - Skill matching indicators
        - Application links
        - Deadline tracking
    """
<<<<<<< HEAD
    st.header("🚀 Opportunity Dashboard")
    st.write("Explore career opportunities")

=======
    st.header(f"🚀 {get_text('opportunities', st.session_state.language)}")
    st.write(get_text("explore_opportunities", st.session_state.language))
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    # Search and filters
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
<<<<<<< HEAD
        search_query = st.text_input("Search opportunities", placeholder="e.g., internship, python, data science")

    with col2:
        opportunity_type = st.selectbox("Type", ["All", "internship", "bootcamp", "competition", "job"])

    with col3:
        category = st.selectbox("Category", ["All", "tech", "data", "business", "learning", "security"])

=======
        search_query = st.text_input(
            get_text("search_opportunities", st.session_state.language),
            placeholder=get_text("search_placeholder", st.session_state.language)
        )
    
    with col2:
        opportunity_type = st.selectbox(
            get_text("type", st.session_state.language),
            ["All", "internship", "bootcamp", "competition", "job"]
        )
    
    with col3:
        category = st.selectbox(
            get_text("category", st.session_state.language),
            ["All", "tech", "data", "business", "learning", "security"]
        )
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    st.markdown("---")

    try:
        opportunity_engine = OpportunityEngine()

        filters = {}
        if opportunity_type != "All":
            filters["type"] = opportunity_type
        if category != "All":
            filters["category"] = category

        if search_query:
            opportunities = opportunity_engine.search_opportunities(search_query, filters)
        else:
            skills = st.session_state.resume_data.get("skills", []) if st.session_state.resume_data else []
            education = st.session_state.user_profile.get("education_level", "UG")
            experience = st.session_state.user_profile.get("experience_years", 0)

            opportunities = opportunity_engine.recommend_opportunities(
                user_skills=skills, education_level=education, experience_years=experience, preferences=filters
            )
    except Exception as exc:
        logger.exception("Opportunities failed, using fallback dataset: %s", exc)
        st.warning("Opportunity service unavailable. Showing fallback results.")
        opportunities = fallback_opportunities()

    # Display opportunities
    if opportunities:
        st.success(f"✅ {get_text('opportunities_found', st.session_state.language).format(count=len(opportunities))}")
        st.markdown("---")

        for idx, opp in enumerate(opportunities, 1):
            with st.container():
                col1, col2 = st.columns([3, 1])

                with col1:
                    st.markdown(f"### {idx}. {opp.get('opportunity_name', 'Opportunity')}")

                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        st.write(f"**{get_text('opportunity_type', st.session_state.language)}:** {opp.get('opportunity_type', 'N/A')}")
                    with col_b:
                        st.write(f"**{get_text('category', st.session_state.language)}:** {opp.get('category', 'N/A')}")
                    with col_c:
<<<<<<< HEAD
                        st.write(f"**Deadline:** {opp.get('deadline', 'N/A')}")

                    if "match_score" in opp:
                        st.write(f"**Match Score:** {opp['match_score']}%")

                    if opp.get("stipend_or_prize"):
                        st.write(f"**Stipend/Prize:** ₹{opp['stipend_or_prize']:,}")

                    # Skills
                    if opp.get("required_skills"):
                        st.markdown("**Required Skills:** " + ", ".join(opp["required_skills"]))

                with col2:
                    if st.button("Apply Now", key=f"apply_opp_{idx}"):
                        st.success("Redirecting to application...")

=======
                        st.write(f"**{get_text('deadline', st.session_state.language)}:** {opp.get('deadline', 'N/A')}")
                    
                    if "match_score" in opp:
                        st.write(f"**{get_text('match_score_label', st.session_state.language)}:** {opp['match_score']}%")
                    
                    if opp.get("stipend_or_prize"):
                        st.write(f"**{get_text('stipend_prize', st.session_state.language)}:** ₹{opp['stipend_or_prize']:,}")
                    
                    # Skills
                    if opp.get("required_skills"):
                        st.markdown(f"**{get_text('required_skills', st.session_state.language)}:** " + ", ".join(opp["required_skills"]))
                
                with col2:
                    if st.button(get_text("apply_now", st.session_state.language), key=f"apply_opp_{idx}"):
                        st.success(get_text("redirecting", st.session_state.language))
                
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
                st.divider()
    else:
        st.info(get_text("no_opportunities", st.session_state.language))


def render_roadmap_generator() -> None:
    """
    Render Learning Roadmap Generator page.

    Creates personalized learning plans.

    TODO: Implement roadmap generator page with:
        - User profile form
        - Learning plan generation
        - Monthly goals display
        - Skill priorities
        - Resource recommendations
        - Progress tracking
    """
<<<<<<< HEAD
    st.header("🗺️ Learning Roadmap Generator")
    st.write("Create your personalized learning roadmap")

=======
    st.header(f"🗺️ {get_text('learning_roadmap', st.session_state.language)}")
    st.write(get_text("create_learning_roadmap", st.session_state.language))
    
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
    # Input form
    col1, col2 = st.columns(2)

    with col1:
        target_career = st.selectbox(
<<<<<<< HEAD
            "Target Career",
            ["Data Scientist", "Software Developer", "DevOps Engineer", "Full Stack Developer", "ML Engineer"],
        )
        available_hours = st.slider("Available Hours per Week", min_value=5, max_value=40, value=15, step=5)

    with col2:
        duration_months = st.slider("Learning Duration (months)", min_value=1, max_value=24, value=6)
        st.selectbox("Preferred Pace", ["Beginner", "Intermediate", "Advanced"])

    st.markdown("---")

    if st.button("Generate Learning Roadmap", key="generate_roadmap"):
        current_skills = st.session_state.resume_data.get("skills", []) if st.session_state.resume_data else []
        try:
            with st.spinner("Creating your personalized roadmap..."):
                roadmap_engine = RoadmapGenerator()
                learning_plan = roadmap_engine.generate_learning_plan(
                    current_skills=current_skills,
                    target_career=target_career,
                    available_hours_per_week=available_hours,
                    duration_months=duration_months,
                )
        except Exception as exc:
            logger.exception("Roadmap generation failed, using fallback roadmap: %s", exc)
            st.warning("Learning roadmap service unavailable. Showing fallback results.")
            learning_plan = fallback_learning_plan(current_skills, target_career, available_hours, duration_months)

        st.session_state.learning_plan = learning_plan

        st.success("✅ Roadmap generated successfully!")
=======
            get_text("target_career", st.session_state.language),
            ["Data Scientist", "Software Developer", "DevOps Engineer", "Full Stack Developer", "ML Engineer"]
        )
        available_hours = st.slider(
            get_text("available_hours", st.session_state.language),
            min_value=5,
            max_value=40,
            value=15,
            step=5
        )
    
    with col2:
        duration_months = st.slider(
            get_text("learning_duration", st.session_state.language),
            min_value=1,
            max_value=24,
            value=6
        )
        learning_pace = st.selectbox(
            get_text("preferred_pace", st.session_state.language),
            ["Beginner", "Intermediate", "Advanced"]
        )
    
    st.markdown("---")
    
    if st.button(get_text("generate_roadmap", st.session_state.language), key="generate_roadmap"):
        with st.spinner(get_text("loading", st.session_state.language)):
            roadmap_engine = RoadmapGenerator()
            
            # Get current skills
            current_skills = st.session_state.resume_data.get("skills", []) if st.session_state.resume_data else []
            
            # Generate plan
            learning_plan = roadmap_engine.generate_learning_plan(
                current_skills=current_skills,
                target_career=target_career,
                available_hours_per_week=available_hours,
                duration_months=duration_months
            )
        
        st.session_state.learning_plan = learning_plan
        
        st.success(get_text("roadmap_generated", st.session_state.language))
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        st.markdown("---")

        # Display learning plan summary
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(get_text("target_career", st.session_state.language), target_career)
        with col2:
            st.metric(get_text("duration", st.session_state.language), f"{duration_months} months")
        with col3:
            st.metric(get_text("weekly_hours", st.session_state.language), f"{available_hours} hrs")
        with col4:
            total_hours = available_hours * 4 * duration_months
<<<<<<< HEAD
            st.metric("Total Hours", total_hours)

=======
            st.metric(get_text("total_hours", st.session_state.language), total_hours)
        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        st.markdown("---")

        # Skill gap analysis
        st.markdown(f"## {get_text('skill_gap_analysis', st.session_state.language)}")
        current = learning_plan.get("current_skills", [])
        target = learning_plan.get("target_skills", [])
        missing = learning_plan.get("missing_skills", [])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"**{get_text('current_skills', st.session_state.language)}:** {len(current)}")
            for skill in current:
                st.write(f"✅ {skill}")

        with col2:
            st.write(f"**{get_text('target_skills', st.session_state.language)}:** {len(target)}")
            for skill in target:
                st.write(f"🎯 {skill}")

        with col3:
            st.write(f"**{get_text('skills_to_learn', st.session_state.language)}:** {len(missing)}")
            for skill in missing:
                st.write(f"📚 {skill}")

        st.markdown("---")

        # Monthly breakdown
        st.markdown(f"## {get_text('monthly_breakdown', st.session_state.language)}")
        monthly_goals = learning_plan.get("monthly_goals", [])
<<<<<<< HEAD

=======
        
        if not monthly_goals:
            st.warning(get_text("no_roadmap_generated", st.session_state.language))
            return
        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        for month_data in monthly_goals:
            month = month_data.get("month", 1)
            title = month_data.get("title", f"Month {month}")
            skills = month_data.get("skills_to_develop", [])
            topics = month_data.get("topics_to_learn", [])
            projects = month_data.get("projects_to_build", [])
            hours = month_data.get("estimated_hours", 0)
<<<<<<< HEAD

            with st.expander(f"Month {month}: {', '.join(skills[:2])}{'...' if len(skills) > 2 else ''}"):
                st.write(f"**Estimated Hours:** {hours}")
                st.write("**Skills to Develop:**")
                for skill in skills:
                    st.write(f"• {skill}")

                # Get resources
                roadmap_engine = RoadmapGenerator()
                resources = []
                for skill in skills:
                    skill_resources = roadmap_engine.recommend_resources(skill)
                    resources.extend(skill_resources)

                if resources:
                    st.write("**Recommended Resources:**")
                    for res in resources[:5]:
                        st.write(f"• {res['name']}")

=======
            resources = month_data.get("resources", [])
            
            # Create a comprehensive expander for each month
            with st.expander(f"📅 {title}"):
                # Hours metric
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("⏱️ " + get_text('estimated_hours', st.session_state.language), f"{hours} hrs")
                with col2:
                    st.metric("🎯 " + get_text('skills_to_develop', st.session_state.language), len(skills))
                with col3:
                    st.metric("📚 " + get_text('topics', st.session_state.language), len(topics))
                
                st.divider()
                
                # Skills section
                if skills:
                    st.markdown(f"**🎯 {get_text('skills_to_develop', st.session_state.language)}:**")
                    skill_cols = st.columns(min(3, len(skills)))
                    for idx, skill in enumerate(skills):
                        with skill_cols[idx % len(skill_cols)]:
                            st.write(f"• {skill}")
                else:
                    st.info("No skills to develop this month")
                
                st.divider()
                
                # Topics section
                if topics:
                    st.markdown(f"**📖 {get_text('topics_to_learn', st.session_state.language)}:**")
                    for topic in topics:
                        st.write(f"✓ {topic}")
                else:
                    st.info("Review topics from previous months")
                
                st.divider()
                
                # Projects section
                if projects:
                    st.markdown(f"**💻 {get_text('projects_to_build', st.session_state.language)}:**")
                    for idx, project in enumerate(projects, 1):
                        st.write(f"{idx}. {project}")
                else:
                    st.info("Practice exercises")
                
                st.divider()
                
                # Resources section
                if resources:
                    st.markdown(f"**📚 {get_text('recommended_resources', st.session_state.language)}:**")
                    for resource in resources:
                        st.write(f"• {resource}")
                else:
                    st.info("Use Google, YouTube, and documentation")
        
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
        st.markdown("---")

        # Action buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(get_text("download_roadmap", st.session_state.language), key="download_roadmap"):
                st.success("Roadmap downloaded!")

        with col2:
            if st.button(get_text("start_learning", st.session_state.language), key="start_learning"):
                st.success("Start with the first month's goals!")

        with col3:
            if st.button(get_text("share_roadmap", st.session_state.language), key="share_roadmap"):
                st.success("Share link copied to clipboard!")


<<<<<<< HEAD
def render_ai_career_assistant() -> None:
    """
    Render AI-powered career assistant page.

    Supports local Ollama, BYOK providers, and a rule-based fallback.
    """
    st.header(t("ai_career_assistant"))
    st.write(t("career_subtitle"))

    language = selected_language()
    st.info(f"{t('selected_response_language')}: **{language}**")

    with st.expander(t("ai_provider_settings"), expanded=True):
        provider = st.radio(
            "Provider",
            ["Auto", "BYOK", "Local Ollama", "Rule-based fallback"],
            horizontal=True,
            help="Auto tries cloud API first, then local Ollama, then offline fallback.",
        )

        col1, col2 = st.columns(2)
        with col1:
            if provider in {"BYOK", "Auto"}:
                model_name = st.text_input(
                    "Model name",
                    value=get_runtime_setting("BYOK_MODEL", DEFAULT_BYOK_MODEL),
                    help="Use the model name supported by your provider.",
                )
            else:
                model_name = st.text_input(
                    "Ollama model name",
                    value=get_runtime_setting("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL),
                    help="Default is llama3. Example: llama3, mistral, gemma.",
                )

        with col2:
            if provider in {"BYOK", "Auto"}:
                byok_endpoint = st.text_input(
                    "BYOK API endpoint",
                    value=get_runtime_setting("BYOK_API_URL", DEFAULT_BYOK_ENDPOINT),
                    help="OpenAI-compatible chat completions endpoint.",
                )
                if provider == "Auto":
                    st.text_input(
                        "Ollama API URL",
                        value=get_runtime_setting("OLLAMA_API_URL", OLLAMA_GENERATE_URL),
                        key="ollama_url_input",
                        help="Optional local fallback endpoint. Streamlit Cloud usually cannot reach localhost.",
                    )
            else:
                byok_endpoint = DEFAULT_BYOK_ENDPOINT
                st.text_input(
                    "Ollama API URL",
                    value=get_runtime_setting("OLLAMA_API_URL", OLLAMA_GENERATE_URL),
                    key="ollama_url_input",
                    help="Local Ollama generate endpoint.",
                )

        if provider in {"BYOK", "Auto"}:
            api_token = st.text_input(
                "API key/token",
                value=get_runtime_setting("BYOK_API_KEY", ""),
                type="password",
                help="Your token is used only for this Streamlit session and is not saved in the repository.",
            )
            ollama_url = st.session_state.get("ollama_url_input", OLLAMA_GENERATE_URL)
        else:
            api_token = ""
            ollama_url = st.session_state.get("ollama_url_input", OLLAMA_GENERATE_URL)

    st.markdown(f"### {t('your_question')}")
    question = st.text_area(
        t("ask_career_related"),
        placeholder=t("career_question_placeholder"),
        height=130,
    )

    resume_skills = st.session_state.resume_data.get("skills", []) if st.session_state.resume_data else []
    profile = {
        **st.session_state.user_profile,
        "skills": st.session_state.user_profile.get("skills") or resume_skills,
    }

    if st.button(t("generate_ai_guidance"), key="generate_ai_guidance"):
        config = AIProviderConfig(
            provider=provider,
            language=language,
            model_name=model_name,
            ollama_url=ollama_url,
            api_token=api_token,
            byok_endpoint=byok_endpoint,
        )

        with st.spinner(t("generating_career_guidance")):
            st.session_state.ai_assistant_response = generate_ai_response(question, config, profile)
            st.session_state.ai_assistant_warning = is_ai_warning_response(st.session_state.ai_assistant_response)

    if st.session_state.ai_assistant_response:
        st.markdown("---")
        st.markdown(f"### {t('ai_guidance')}")
        if st.session_state.get("ai_assistant_warning"):
            st.warning(st.session_state.ai_assistant_response)
            return
        st.markdown(st.session_state.ai_assistant_response)


def is_ai_warning_response(response: str) -> bool:
    """Detect provider errors that should be shown as Streamlit warnings."""
    warning_markers = [
        "AI service unavailable",
        "Please enter",
        "I could not connect",
        "I could not reach",
        "took too long",
        "returned an error",
        "returned an HTTP error",
        "returned an invalid response",
        "returned an empty response",
    ]
    return any(marker in response for marker in warning_markers)


def selected_language() -> str:
    """Return the selected UI language with a safe fallback."""
    return normalize_language(st.session_state.get("language") or st.session_state.get("selected_language", "English"))


def t(key: str) -> str:
    """Translate a UI label using the selected language."""
    return translate(key, selected_language())


def sync_language_state() -> None:
    """Keep the UI language and AI response language in sync after dropdown changes."""
    selected = st.session_state.get("language_selector", "English")
    st.session_state.language = normalize_language(selected)
    st.session_state.selected_language = st.session_state.language


def render_sidebar() -> str:
    """Render sidebar navigation with translated labels but stable route values."""
    st.sidebar.title("Career Bridge AI")
    st.sidebar.write(t("app_tagline"))
    st.sidebar.divider()

    page_keys = [
        "Home",
        "Resume Analyzer",
        "Career Mentor",
        "Scholarship Finder",
        "Government Schemes",
        "Opportunities",
        "Learning Roadmap",
        "AI Career Assistant",
        "Deployment Diagnostics",
    ]
    page_translation_keys = {
        "Home": "home",
        "Resume Analyzer": "resume_analyzer",
        "Career Mentor": "career_mentor",
        "Scholarship Finder": "scholarship_finder",
        "Government Schemes": "government_schemes",
        "Opportunities": "opportunities",
        "Learning Roadmap": "learning_roadmap",
        "AI Career Assistant": "ai_career_assistant",
        "Deployment Diagnostics": "deployment_diagnostics",
    }

    page = st.sidebar.radio(
        t("navigation"),
        options=page_keys,
        index=0,
        format_func=lambda page_name: t(page_translation_keys[page_name]),
    )

    render_language_selector()

    st.sidebar.divider()
    st.sidebar.markdown(f"### {t('quick_links')}")
    st.sidebar.markdown(f"[{t('documentation')}](https://github.com/CareerBridgeAI)")
    st.sidebar.markdown(f"[{t('report_issue')}](https://github.com/CareerBridgeAI/issues)")
    st.sidebar.markdown(f"[{t('contact_us')}](mailto:support@careerbridgeai.com)")

    return page


def render_language_selector() -> None:
    """Render language selector without conflicting session_state defaults."""
    st.sidebar.divider()
    language_options = get_language_names()

    if "language" not in st.session_state or st.session_state.language not in language_options:
        st.session_state.language = normalize_language(st.session_state.get("selected_language", "English"))

    if "language_selector" not in st.session_state or st.session_state.language_selector not in language_options:
        st.session_state.language_selector = st.session_state.language

    st.sidebar.selectbox(
        t("language"),
        options=language_options,
        key="language_selector",
        on_change=sync_language_state,
        help="AI Career Assistant responses and main UI labels use this language.",
    )


def render_home_page() -> None:
    """Render a translated landing dashboard for the selected language."""
    st.title(t("home_title"))
    st.write(t("home_subtitle"))
    st.info(t("home_intro"))

    st.markdown(f"### {t('main_features')}")
    feature_keys = [
        "resume_analyzer",
        "career_mentor",
        "scholarship_finder",
        "government_schemes",
        "opportunities",
        "learning_roadmap",
        "ai_career_assistant",
    ]
    cols = st.columns(2)
    for index, feature_key in enumerate(feature_keys):
        with cols[index % 2]:
            st.write(f"- **{t(feature_key)}**")


def render_deployment_diagnostics() -> None:
    """Show deployment health without requiring local-only services."""
    st.header(t("deployment_diagnostics"))
    st.write("Deployment-safe status checks for demo readiness.")

    checks = []
    byok_token = bool(get_runtime_setting("BYOK_API_KEY", ""))
    byok_url = get_runtime_setting("BYOK_API_URL", DEFAULT_BYOK_ENDPOINT)
    ollama_url = get_runtime_setting("OLLAMA_API_URL", OLLAMA_GENERATE_URL)

    checks.append(("Cloud AI API key", "Configured" if byok_token else "Missing - fallback will be used"))
    checks.append(("Cloud AI endpoint", byok_url or "Not configured"))
    checks.append(("Ollama endpoint", ollama_url if "localhost" not in ollama_url else "Local only - skipped in cloud unless available"))

    try:
        db = get_db_manager()
        checks.append(("Database", "Available" if getattr(db, "available", False) else "Unavailable - app will use session fallbacks"))
    except Exception as exc:
        logger.warning("Diagnostics database check failed: %s", exc)
        checks.append(("Database", "Unavailable - app will use session fallbacks"))

    parser_packages = []
    for package_name in ["pypdf", "PyPDF2", "pdfplumber", "docx"]:
        try:
            __import__(package_name)
            parser_packages.append(f"{package_name}: ok")
        except Exception:
            parser_packages.append(f"{package_name}: missing")
    checks.append(("File upload parsers", ", ".join(parser_packages)))

    for label, status in checks:
        if "Missing" in status or "Unavailable" in status or "missing" in status:
            st.warning(f"**{label}:** {status}")
        else:
            st.success(f"**{label}:** {status}")

    st.info("If a cloud service is missing, Career Bridge AI will continue with local datasets and rule-based fallback logic.")


def fallback_scholarships(education_level: str, annual_income: float) -> list[dict[str, object]]:
    """Return sample scholarships when the deployed data layer is unavailable."""
    results = []
    for row in DEFAULT_SCHOLARSHIPS:
        education_match = education_level.lower() in str(row.get("education", "")).lower()
        income_match = annual_income <= float(row.get("max_income", 0))
        if education_match and income_match:
            results.append(
                {
                    "scholarship_name": row["name"],
                    "award_amount": row["award"],
                    "eligibility": "Eligible",
                    "deadline": row["deadline"],
                    "match_score": 80,
                }
            )
    return results or [
        {
            "scholarship_name": DEFAULT_SCHOLARSHIPS[0]["name"],
            "award_amount": DEFAULT_SCHOLARSHIPS[0]["award"],
            "eligibility": "Review eligibility",
            "deadline": DEFAULT_SCHOLARSHIPS[0]["deadline"],
            "match_score": 60,
        }
    ]


def fallback_schemes(annual_income: float, age: int) -> list[dict[str, object]]:
    """Return sample government schemes when the deployed data layer is unavailable."""
    results = []
    for row in DEFAULT_SCHEMES:
        if annual_income <= float(row.get("max_income", 0)) and age <= int(row.get("age_limit", 100)):
            results.append(
                {
                    "scheme_name": row["name"],
                    "scheme_type": row["type"],
                    "benefit": row["benefit"],
                    "eligibility": "Eligible",
                    "deadline": row["deadline"],
                    "max_income": row["max_income"],
                    "age_limit": row["age_limit"],
                }
            )
    return results or [
        {
            "scheme_name": DEFAULT_SCHEMES[0]["name"],
            "scheme_type": DEFAULT_SCHEMES[0]["type"],
            "benefit": DEFAULT_SCHEMES[0]["benefit"],
            "eligibility": "Review eligibility",
            "deadline": DEFAULT_SCHEMES[0]["deadline"],
            "max_income": DEFAULT_SCHEMES[0]["max_income"],
            "age_limit": DEFAULT_SCHEMES[0]["age_limit"],
        }
    ]


def fallback_opportunities() -> list[dict[str, object]]:
    """Return sample opportunities when deployed data/search is unavailable."""
    return [
        {
            "opportunity_name": row["name"],
            "opportunity_type": row["type"],
            "category": row["category"],
            "required_skills": [skill.strip() for skill in row.get("skills", "").split(",")],
            "deadline": row["deadline"],
            "stipend_or_prize": row.get("stipend") or row.get("prize"),
            "match_score": 65,
        }
        for row in DEFAULT_OPPORTUNITIES
    ]


def fallback_learning_plan(
    current_skills: list[str],
    target_career: str,
    available_hours: int,
    duration_months: int,
) -> dict[str, object]:
    """Return a simple roadmap when roadmap generation is unavailable."""
    target_skills = ["python", "sql", "git", "projects"]
    current_lower = [skill.lower() for skill in current_skills]
    missing_skills = [skill for skill in target_skills if skill not in current_lower]
    return {
        "target_career": target_career,
        "current_skills": current_skills,
        "target_skills": target_skills,
        "missing_skills": missing_skills,
        "duration_months": duration_months,
        "available_hours_per_week": available_hours,
        "monthly_goals": [
            {
                "month": month,
                "skills_to_develop": missing_skills[:2] or target_skills[:2],
                "estimated_hours": available_hours * 4,
            }
            for month in range(1, duration_months + 1)
        ],
    }


def render_resume_analyzer() -> None:
    """Render a robust resume analyzer with readable-file handling."""
    st.header(t("resume_header"))
    st.write(t("resume_subtitle"))

    uploaded_file = st.file_uploader(t("resume_upload"), type=["pdf", "docx", "txt"])

    if uploaded_file is None:
        return

    try:
        parser = ResumeParser.from_upload(uploaded_file)

        with st.spinner(t("resume_spinner")):
            text = parser.extract_text()
            if parser.metadata.get("used_fallback_parser"):
                st.warning("Using fallback resume parser for deployment compatibility.")
            if not parser.has_enough_resume_text(text):
                if uploaded_file.name.lower().endswith(".pdf"):
                    st.warning("Could not extract enough text from this PDF. Please try TXT/DOCX resume.")
                else:
                    st.warning(t("resume_extract_error"))
                return
            skills = parser.extract_skills()
            education = parser.extract_education()
            experience = parser.extract_experience()
            ats_score = parser.calculate_ats_score()
    except ValueError as exc:
        logger.warning("Unsupported resume upload: %s", exc)
        st.error(t("resume_format_error"))
        return
    except Exception as exc:
        logger.exception("Resume analysis failed: %s", exc)
        st.error(t("resume_general_error"))
        return

    st.session_state.resume_data = {
        "text": text,
        "skills": skills,
        "education": education,
        "experience": experience,
        "ats_score": ats_score,
    }
    st.session_state.user_profile["skills"] = skills

    st.success(t("resume_success"))
    col1, col2, col3 = st.columns(3)
    col1.metric(t("ats_score"), f"{ats_score:.1f}/100", delta=t("good") if ats_score > 70 else t("needs_improvement"))
    col2.metric(t("skills_found"), len(skills), delta=f"+{len(skills)}")
    col3.metric(t("education"), len(education), delta=t("complete") if education else t("missing"))

    st.markdown("---")
    st.markdown(f"## {t('extracted_skills')}")
    if skills:
        for skill in sorted(skills):
            st.write(f"- {skill}")
    else:
        st.warning(t("no_skills_detected"))

    st.markdown(f"## {t('skill_gaps')}")
    resume_recommendations = get_career_recommendations_safely(
        user_skills=skills,
        education=education[0].get("type", "Not provided") if education else "Not provided",
        experience_years=len(experience),
        preferences={"domain": "resume"},
    )
    top_recommendation = resume_recommendations[0] if resume_recommendations else {}
    missing_skills = top_recommendation.get("missing_skills") or []
    if missing_skills:
        for skill in missing_skills:
            st.write(f"- {skill}")
    else:
        st.success(t("no_major_gap"))

    st.markdown(f"## {t('education')}")
    if education:
        for edu in education:
            st.write(f"- {edu.get('type', 'Degree')}")
    else:
        st.info(t("no_education"))

    st.markdown(f"## {t('work_experience')}")
    if experience:
        for exp in experience:
            st.write(f"- {exp.get('title', 'Position')}")
    else:
        st.info(t("no_experience"))

    st.markdown(f"## {t('improvement_suggestions')}")
    suggestions = []
    if ats_score < 50:
        suggestions.append(t("suggest_keywords"))
    if len(skills) < 5:
        suggestions.append(t("suggest_skills"))
    if not education:
        suggestions.append(t("suggest_education"))
    if not experience:
        suggestions.append(t("suggest_experience"))

    if suggestions:
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
    else:
        st.success(t("resume_good"))

    st.markdown("---")
    st.markdown(f"## {t('career_suggestions')}")
    display_career_cards(resume_recommendations[:3])


def render_career_mentor() -> None:
    """Render career mentor with meaningful fallback recommendations."""
    st.header(t("career_header"))
    st.write(t("career_subtitle"))

    st.markdown(f"### {t('your_profile')}")
    col1, col2 = st.columns(2)
    with col1:
        experience_years = st.slider(t("years_experience"), 0, 50, 2)
        education_level = st.selectbox(t("education_level"), ["10th", "12th", "UG", "PG", "Diploma"])
    with col2:
        career_domain = st.selectbox(
            t("career_domain"),
            ["Software", "Data", "AI/ML", "Web Development", "Cloud", "Cybersecurity", "Business"],
        )
        interests = st.text_input(t("interests"), placeholder="AI, web development, data, government jobs")

    skill_options = [
        "python",
        "java",
        "javascript",
        "sql",
        "machine learning",
        "data analysis",
        "web development",
        "cloud computing",
        "communication",
        "leadership",
        "problem solving",
        "testing",
        "html",
        "css",
        "git",
    ]
    resume_skills = st.session_state.resume_data.get("skills", []) if st.session_state.resume_data else []
    default_skills = [skill for skill in resume_skills if skill in skill_options]

    skills_input = st.multiselect(
        t("your_skills"),
        options=skill_options,
        default=default_skills,
    )
    goals = st.text_area(t("career_goals"), placeholder="Example: I want an entry-level tech job in 6 months.", height=90)

    st.session_state.user_profile["education_level"] = education_level
    st.session_state.user_profile["experience_years"] = experience_years
    st.session_state.user_profile["skills"] = skills_input
    st.session_state.user_profile["interests"] = interests
    st.session_state.user_profile["goals"] = goals

    if st.button(t("get_career_recommendation"), key="career_recommendations_widget"):
        with st.spinner(t("recommendation_spinner")):
            recommendations = get_career_recommendations_safely(
                user_skills=skills_input,
                education=education_level,
                experience_years=experience_years,
                preferences={"domain": career_domain, "interests": interests, "goals": goals},
            )
        st.session_state.career_recommendations_data = recommendations

    recommendations = st.session_state.get("career_recommendations_data", [])
    if recommendations:
        st.success(t("recommendation_success"))
        display_career_cards(recommendations)
    else:
        st.info(t("recommendation_prompt"))


def clean_display_value(value: object, fallback: str) -> str:
    """Avoid empty, null, or Unknown values in user-facing output."""
    text = str(value).strip() if value is not None else ""
    if not text or text.lower() in {"unknown", "nan", "none", "null"}:
        return fallback
    return text


def get_career_recommendations_safely(
    user_skills: list[str],
    education: str,
    experience_years: int,
    preferences: dict[str, object] | None = None,
) -> list[dict[str, object]]:
    """Return meaningful career recommendations, falling back instead of showing Unknown."""
    career_engine = CareerRecommendationEngine()
    try:
        recommendations = career_engine.recommend_careers(
            user_skills=user_skills,
            education=education,
            experience_years=experience_years,
            preferences=preferences,
        )
    except Exception as exc:
        logger.exception("Career recommendation failed: %s", exc)
        st.warning(t("recommendation_fallback"))
        return career_engine.generate_fallback_recommendations(
            user_skills=user_skills,
            education=education,
            experience_years=experience_years,
            preferences=preferences,
        )

    meaningful = [
        rec
        for rec in recommendations
        if clean_display_value(rec.get("career_name"), "") and clean_display_value(rec.get("career_name"), "") != ""
    ]
    if meaningful:
        return meaningful

    st.warning(t("recommendation_fallback"))
    return career_engine.generate_fallback_recommendations(
        user_skills=user_skills,
        education=education,
        experience_years=experience_years,
        preferences=preferences,
    )


def display_career_cards(recommendations: list[dict[str, object]]) -> None:
    """Display career recommendations with skill gaps and next steps."""
    if not recommendations:
        return

    st.markdown("---")
    for idx, rec in enumerate(recommendations, 1):
        career_name = clean_display_value(rec.get("career_name"), t("recommended_career_path"))
        required_skills = rec.get("required_skills") or []
        matching_skills = rec.get("matching_skills") or []
        missing_skills = rec.get("missing_skills") or []
        roadmap = rec.get("learning_roadmap") or []
        next_steps = rec.get("suggested_next_steps") or []

        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {idx}. {career_name}")
                st.write(f"**{t('match_score')}:** {rec.get('match_score', 60)}%")
                st.write(f"**{t('growth_potential')}:** {clean_display_value(rec.get('growth_potential'), 'Promising')}")
                st.write(
                    f"**{t('salary_range')}:** "
                    f"{clean_display_value(rec.get('salary_range'), 'Varies by location and experience')}"
                )
                if rec.get("description"):
                    st.write(str(rec["description"]))

                st.markdown(f"**{t('required_skills')}:** " + (", ".join(required_skills) if required_skills else t("not_available")))
                st.markdown(f"**{t('matching_skills')}:** " + (", ".join(matching_skills) if matching_skills else t("not_available")))
                st.markdown(f"**{t('skill_gaps')}:** " + (", ".join(missing_skills) if missing_skills else t("no_major_gap")))

                if roadmap:
                    st.markdown(f"**{t('recommended_learning_path')}:**")
                    for item in roadmap:
                        st.write(f"- {item}")

                if next_steps:
                    st.markdown(f"**{t('suggested_next_steps')}:**")
                    for item in next_steps:
                        st.write(f"- {item}")

            with col2:
                if rec.get("source") == "fallback":
                    st.info(t("rule_based_fallback"))
                if st.button(t("learn_more"), key=f"career_more_{idx}_{career_name}"):
                    st.info(
                        f"{t('recommended_career_path')}: {career_name}\n\n"
                        f"{t('required_skills')}: {', '.join(required_skills) if required_skills else t('core_role_skills')}"
                    )
            st.divider()
=======
def render_ai_assistant() -> None:
    """
    Render AI Career Assistant page.
    
    Provides AI-powered career guidance using Ollama or BYOK provider.
    Features:
    - Ask career questions
    - Generate career roadmap
    - Resume improvement tips
    - Interview questions
    - Skill recommendations
    - Project suggestions
    """
    st.header(get_text("ai_assistant", st.session_state.language))
    st.write(get_text("ai_assistant_desc", st.session_state.language))
    
    # Initialize AI service if not already done
    if st.session_state.ai_service is None:
        try:
            if st.session_state.ai_provider.lower() == "ollama":
                # Check if Ollama is running
                ollama = OllamaProvider(OLLAMA_MODEL)
                if not ollama.check_connection():
                    st.error(get_text("ollama_not_running", st.session_state.language))
                    st.info("To use Ollama, download it from: https://ollama.ai")
                    return
                st.session_state.ai_service = create_ai_service("ollama", OLLAMA_MODEL)
            elif st.session_state.ai_provider.lower() == "byok":
                if not BYOK_API_KEY:
                    st.warning("BYOK provider configured but no API key found. Please configure in Settings.")
                    return
                st.session_state.ai_service = create_ai_service("byok", byok_api_key=BYOK_API_KEY)
        except Exception as e:
            st.error(f"Error initializing AI service: {e}")
            return
    
    if st.session_state.ai_service is None:
        st.error("AI service not available. Please check your settings.")
        return
    
    # AI Assistant interface
    st.markdown("### " + get_text("ai_assistant", st.session_state.language))
    
    # Tabs for different AI features
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "💬 " + get_text("question", st.session_state.language),
        "🗺️ " + get_text("generate_career_roadmap", st.session_state.language),
        "📝 " + get_text("resume_tips", st.session_state.language),
        "🎯 " + get_text("interview_questions", st.session_state.language),
        "📚 " + get_text("skill_recommendations", st.session_state.language),
        "💻 " + get_text("project_suggestions", st.session_state.language)
    ])
    
    with tab1:
        st.markdown(f"#### {get_text('ask_question', st.session_state.language)}")
        question = st.text_area(
            get_text("question", st.session_state.language),
            placeholder=get_text("question_placeholder", st.session_state.language),
            height=100
        )
        
        if st.button(get_text("get_ai_response", st.session_state.language), key="ai_question"):
            if question.strip():
                with st.spinner(get_text("loading", st.session_state.language)):
                    try:
                        response = st.session_state.ai_service.generate_career_advice(question)
                        if response:
                            st.success(get_text("ai_response", st.session_state.language))
                            st.write(response)
                            st.session_state.chat_history.append({
                                "question": question,
                                "response": response,
                                "type": "career_advice"
                            })
                        else:
                            st.error(get_text("ollama_connection_error", st.session_state.language))
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning(get_text("enter_question", st.session_state.language))
    
    with tab2:
        st.markdown(f"#### {get_text('generate_career_roadmap', st.session_state.language)}")
        target_career = st.text_input(
            get_text("target_career_label", st.session_state.language),
            placeholder=get_text("target_career_placeholder", st.session_state.language)
        )
        current_level = st.select_slider(
            get_text("current_level", st.session_state.language),
            options=["Beginner", "Intermediate", "Advanced"]
        )
        duration = st.slider(get_text("timeline", st.session_state.language), 1, 24, 6)
        
        if st.button(get_text("generate_roadmap", st.session_state.language), key="ai_roadmap"):
            if target_career.strip():
                with st.spinner(get_text("loading", st.session_state.language)):
                    try:
                        roadmap = st.session_state.ai_service.generate_learning_roadmap(
                            target_career, current_level, duration
                        )
                        if roadmap:
                            st.success(get_text("ai_roadmap_generated", st.session_state.language))
                            st.write(roadmap)
                        else:
                            st.error(get_text("ollama_connection_error", st.session_state.language))
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning(get_text("enter_target_career", st.session_state.language))
    
    with tab3:
        st.markdown(f"#### {get_text('resume_improvement', st.session_state.language)}")
        if st.session_state.resume_data and st.session_state.resume_data.get("text"):
            resume_text = st.session_state.resume_data.get("text", "")
            
            if st.button(get_text("analyze_resume", st.session_state.language), key="ai_resume_tips"):
                with st.spinner(get_text("loading", st.session_state.language)):
                    try:
                        tips = st.session_state.ai_service.generate_resume_tips(resume_text)
                        if tips:
                            st.success(get_text("resume_tips", st.session_state.language))
                            st.write(tips)
                        else:
                            st.error(get_text("ollama_connection_error", st.session_state.language))
                    except Exception as e:
                        st.error(f"Error: {e}")
        else:
            st.info(get_text("upload_analyze_resume", st.session_state.language))
    
    with tab4:
        st.markdown(f"#### {get_text('interview_questions_label', st.session_state.language)}")
        job_title = st.text_input(
            get_text("job_title", st.session_state.language),
            placeholder=get_text("job_title_placeholder", st.session_state.language)
        )
        skills = st.multiselect(
            get_text("select_skills", st.session_state.language),
            options=[
                "Python", "Java", "JavaScript", "SQL", "Machine Learning",
                "Web Development", "Cloud Computing", "Data Analysis"
            ]
        )
        
        if st.button(get_text("generate_questions", st.session_state.language), key="ai_interview"):
            if job_title.strip() and skills:
                with st.spinner(get_text("loading", st.session_state.language)):
                    try:
                        questions = st.session_state.ai_service.generate_interview_questions(
                            job_title, skills
                        )
                        if questions:
                            st.success(get_text("interview_q_a", st.session_state.language))
                            st.write(questions)
                        else:
                            st.error(get_text("ollama_connection_error", st.session_state.language))
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning(get_text("enter_job_and_skills", st.session_state.language))
    
    with tab5:
        st.markdown(f"#### {get_text('skill_recommendations_label', st.session_state.language)}")
        current_skills = st.multiselect(
            get_text("current_skills_label", st.session_state.language),
            options=[
                "Python", "Java", "JavaScript", "SQL", "Machine Learning",
                "Web Development", "Cloud Computing", "Data Analysis",
                "Communication", "Leadership", "Problem Solving"
            ]
        )
        target_role = st.text_input(
            get_text("target_role", st.session_state.language),
            placeholder=get_text("target_career_placeholder", st.session_state.language)
        )
        
        if st.button(get_text("get_recommendations", st.session_state.language), key="ai_skills"):
            if current_skills and target_role.strip():
                with st.spinner(get_text("loading", st.session_state.language)):
                    try:
                        recommendations = st.session_state.ai_service.generate_skill_recommendations(
                            current_skills, target_role
                        )
                        if recommendations:
                            st.success(get_text("recommended_skills", st.session_state.language))
                            st.write(recommendations)
                        else:
                            st.error(get_text("ollama_connection_error", st.session_state.language))
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning(get_text("select_skills_and_role", st.session_state.language))
    
    with tab6:
        st.markdown(f"#### {get_text('project_ideas', st.session_state.language)}")
        skills = st.multiselect(
            get_text("your_skills", st.session_state.language),
            options=[
                "Python", "Java", "JavaScript", "SQL", "Machine Learning",
                "Web Development", "Cloud Computing", "Data Analysis",
                "React", "Django", "Flask", "FastAPI"
            ],
            key="project_skills"
        )
        level = st.select_slider(
            get_text("experience_level", st.session_state.language),
            options=["Beginner", "Intermediate", "Advanced"]
        )
        
        if st.button(get_text("get_project_ideas", st.session_state.language), key="ai_projects"):
            if skills:
                with st.spinner(get_text("loading", st.session_state.language)):
                    try:
                        projects = st.session_state.ai_service.generate_project_suggestions(
                            skills, level
                        )
                        if projects:
                            st.success(get_text("recommended_projects", st.session_state.language))
                            st.write(projects)
                        else:
                            st.error(get_text("ollama_connection_error", st.session_state.language))
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning(get_text("select_skill", st.session_state.language))


def render_settings() -> None:
    """
    Render Settings page.
    
    Allows users to configure:
    - Language preferences
    - AI provider selection
    - Ollama model selection
    - BYOK API key configuration
    """
    st.header(get_text("settings", st.session_state.language))
    
    st.markdown(f"### {get_text('language', st.session_state.language)}")
    
    language_options = get_supported_languages()
    selected_lang_name = st.selectbox(
        get_text("select_language", st.session_state.language),
        options=list(language_options.keys()),
        index=list(language_options.values()).index(st.session_state.language)
    )
    st.session_state.language = language_options[selected_lang_name]
    st.success(f"{get_text('language_set', st.session_state.language)} {selected_lang_name}")
    
    st.divider()
    
    st.markdown(f"### {get_text('ai_provider', st.session_state.language)}")
    
    ai_provider = st.radio(
        get_text("select_ai_provider", st.session_state.language),
        options=[get_text("ollama", st.session_state.language), get_text("byok", st.session_state.language)],
        index=0 if AI_PROVIDER.lower() == "ollama" else 1
    )
    
    st.session_state.ai_service = None  # Reset AI service
    
    if get_text("ollama", st.session_state.language) in ai_provider:
        st.markdown(f"#### {get_text('ollama_config', st.session_state.language)}")
        st.info(get_text("ollama_running", st.session_state.language))
        
        # Display available models
        ollama = OllamaProvider()
        if ollama.check_connection():
            st.success(get_text("ollama_success", st.session_state.language))
            
            available_models = ollama.list_available_models()
            if available_models:
                st.write(f"{get_text('available_models', st.session_state.language)} {', '.join(available_models)}")
            
            # Model selection
            model_name = st.text_input(
                get_text("model_name_label", st.session_state.language),
                value=OLLAMA_MODEL,
                placeholder=get_text("model_placeholder", st.session_state.language)
            )
            
            if st.button(get_text("test_connection", st.session_state.language)):
                with st.spinner(get_text("loading", st.session_state.language)):
                    test_response = ollama.generate("What is career guidance?", max_tokens=50)
                    if test_response:
                        st.success(f"{get_text('connection_successful', st.session_state.language)}\n{get_text('sample_response', st.session_state.language)}: {test_response[:100]}...")
                    else:
                        st.error(get_text("connection_failed", st.session_state.language))
        else:
            st.error(get_text("ollama_not_running", st.session_state.language))
            st.markdown(f"""
            **{get_text('ollama_setup', st.session_state.language)}**
            1. Download from https://ollama.ai
            2. Install and run Ollama
            3. Pull a model: `ollama pull llama3`
            4. Ollama will run at http://localhost:11434
            """)
    
    else:
        st.markdown(f"#### {get_text('byok_config', st.session_state.language)}")
        st.warning(get_text("keep_api_secure", st.session_state.language))
        
        api_key = st.text_input(
            get_text("api_key_input", st.session_state.language),
            type="password",
            placeholder=get_text("api_key_placeholder", st.session_state.language),
            value=BYOK_API_KEY if BYOK_API_KEY else ""
        )
        
        provider_type = st.selectbox(
            get_text("provider_type", st.session_state.language),
            options=["OpenAI", "Anthropic", "Other"],
            index=0
        )
        
        if api_key:
            st.info(get_text("api_key_configured", st.session_state.language))
            
            if st.button(get_text("test_api_connection", st.session_state.language)):
                st.info(get_text("api_testing_soon", st.session_state.language))
        else:
            st.warning(get_text("no_api_key", st.session_state.language))
        
        st.markdown(f"""
        **{get_text('byok_setup', st.session_state.language)}**
        1. {get_text('get_api_key', st.session_state.language)}
        2. Paste it above
        3. The key is stored only in your environment
        4. Never commit .env to git
        """)
    
    st.divider()
    
    st.markdown(f"### {get_text('about', st.session_state.language)}")
    st.write(get_text("version", st.session_state.language))
    st.write(get_text("platform_description", st.session_state.language))
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("[GitHub](https://github.com/CareerBridgeAI)")
    
    with col2:
        st.markdown("[Documentation](https://github.com/CareerBridgeAI/docs)")
    
    with col3:
        st.markdown("[Support](mailto:support@careerbridgeai.com)")
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9


def main() -> None:
    """
    Main application entry point.

    Orchestrates page routing and application flow.
    Routes user to appropriate page based on sidebar selection.
    """
    # Ensure directories exist
    ensure_directories()

    # Initialize session state
    initialize_session_state()

    # Initialize database without blocking the UI if persistence is unavailable.
    try:
        get_db_manager()
    except Exception as exc:
        logger.exception("Database initialization failed: %s", exc)
        st.warning("Database is unavailable. The app will continue with in-memory results for this session.")

    # Render sidebar and get selected page
    page = render_sidebar()
<<<<<<< HEAD

    # Route to selected page
    try:
        if page == "Home":
            render_home_page()
        elif page == "Resume Analyzer":
            render_resume_analyzer()
        elif page == "Career Mentor":
            render_career_mentor()
        elif page == "Scholarship Finder":
            render_scholarship_finder()
        elif page == "Government Schemes":
            render_scheme_recommender()
        elif page == "Opportunities":
            render_opportunity_dashboard()
        elif page == "Learning Roadmap":
            render_roadmap_generator()
        elif page == "AI Career Assistant":
            render_ai_career_assistant()
        elif page == "Deployment Diagnostics":
            render_deployment_diagnostics()
        else:
            render_home_page()
    except Exception as exc:
        logger.exception("Page failed to render: %s", exc)
        st.error("This page could not load right now.")
        st.warning("Please try again or use another feature. The rest of Career Bridge AI is still available.")
=======
    
    # Define home page text in current language
    home_text = get_text("home", st.session_state.language)
    resume_text = get_text("resume_analyzer", st.session_state.language)
    career_text = get_text("career_mentor", st.session_state.language)
    ai_text = get_text("ai_assistant", st.session_state.language)
    scholarship_text = get_text("scholarship_finder", st.session_state.language)
    schemes_text = get_text("government_schemes", st.session_state.language)
    opportunities_text = get_text("opportunities", st.session_state.language)
    roadmap_text = get_text("learning_roadmap", st.session_state.language)
    settings_text = get_text("settings", st.session_state.language)
    
    # Route to selected page
    if page == home_text:
        render_home_page()
    elif page == resume_text:
        render_resume_analyzer()
    elif page == career_text:
        render_career_mentor()
    elif page == ai_text:
        render_ai_assistant()
    elif page == scholarship_text:
        render_scholarship_finder()
    elif page == schemes_text:
        render_scheme_recommender()
    elif page == opportunities_text:
        render_opportunity_dashboard()
    elif page == roadmap_text:
        render_roadmap_generator()
    elif page == settings_text:
        render_settings()
    else:
        render_home_page()
>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9


if __name__ == "__main__":
    main()
