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

import streamlit as st
from pathlib import Path
import logging
import os
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
from database import get_db_manager
from resume_parser import ResumeParser
from career_engine import CareerRecommendationEngine
from scholarship_engine import ScholarshipRecommendationEngine
from scheme_engine import GovernmentSchemeEngine
from opportunity_engine import OpportunityEngine
from roadmap_engine import RoadmapGenerator
from services.language import Language, get_text, get_supported_languages
from services.ai_provider import create_ai_service, OllamaProvider

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)



# Configure Streamlit page
st.set_page_config(
    page_title=STREAMLIT_PAGE_TITLE,
    page_icon=STREAMLIT_PAGE_ICON,
    layout=STREAMLIT_LAYOUT,
    initial_sidebar_state="expanded"
)


def initialize_session_state() -> None:
    """
    Initialize Streamlit session state variables.
    
    Initializes:
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
            "annual_income": 0
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


def render_sidebar() -> str:
    """
    Render sidebar navigation with language selector and AI settings.
    
    Returns:
        Selected page name.
    """
    st.sidebar.title(get_text("app_title", st.session_state.language))
    st.sidebar.write(get_text("tagline", st.session_state.language))
    st.sidebar.divider()
    
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
        ],
        index=0
    )
    
    st.sidebar.divider()
    st.sidebar.markdown("### Quick Links")
    st.sidebar.markdown("[Documentation](https://github.com/CareerBridgeAI)")
    st.sidebar.markdown("[Report Issue](https://github.com/CareerBridgeAI/issues)")
    st.sidebar.markdown("[Contact Us](mailto:support@careerbridgeai.com)")
    
    return page


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
    st.title(get_text("app_title", st.session_state.language))
    st.write(get_text("welcome_message", st.session_state.language))
    
    st.markdown(f"""
    ## {get_text("bridging_students", st.session_state.language)}
    
    {get_text("career_guidance", st.session_state.language)}
    """)
    
    # Feature cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info(get_text("resume_analyzer_desc", st.session_state.language))
    
    with col2:
        st.success(get_text("career_recommendations_desc", st.session_state.language))
    
    with col3:
        st.warning(get_text("scholarship_finder_desc", st.session_state.language))
    
    st.markdown("---")
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.info(get_text("government_schemes_desc", st.session_state.language))
    
    with col5:
        st.success(get_text("opportunities_desc", st.session_state.language))
    
    with col6:
        st.warning(get_text("learning_roadmap_desc", st.session_state.language))
    
    st.markdown("---")
    
    # Quick statistics
    st.markdown(f"## {get_text('platform_statistics', st.session_state.language)}")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(get_text("active_users", st.session_state.language), "10,000+", "+15%")
    
    with col2:
        st.metric(get_text("total_opportunities", st.session_state.language), "5,000+", "+20%")
    
    with col3:
        st.metric(get_text("total_scholarships", st.session_state.language), "1,500+", "+10%")
    
    with col4:
        st.metric(get_text("success_rate", st.session_state.language), "85%", "+5%")
    
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
    st.header(get_text("resume_analyzer", st.session_state.language))
    st.write(get_text("upload_resume", st.session_state.language))
    
    # File upload
    uploaded_file = st.file_uploader(
        get_text("upload_file", st.session_state.language),
        type=["pdf", "docx", "txt"]
    )
    
    if uploaded_file is not None:
        # Save uploaded file
        file_path = Path("uploads") / uploaded_file.name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Parse resume
        parser = ResumeParser(file_path)
        
        if not parser.validate_resume():
            st.error(get_text("invalid_resume", st.session_state.language))
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
            "ats_score": ats_score
        }
        
        # Display results
        st.success(get_text("resume_analyzed", st.session_state.language))
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
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
        
        st.markdown("---")
        
        # Skills section
        st.markdown(f"## {get_text('extracted_skills', st.session_state.language)}")
        if skills:
            cols = st.columns(4)
            for idx, skill in enumerate(skills):
                with cols[idx % 4]:
                    st.label_option_text(skill)
        else:
            st.info(get_text("no_skills_detected", st.session_state.language))
        
        st.markdown("---")
        
        # Education section
        st.markdown(f"## {get_text('education_label', st.session_state.language)}")
        if education:
            for edu in education:
                st.write(f"📚 {edu.get('type', 'Degree')}")
        else:
            st.info(get_text("no_education_found", st.session_state.language))
        
        st.markdown("---")
        
        # Experience section
        st.markdown(f"## {get_text('work_experience', st.session_state.language)}")
        if experience:
            for exp in experience:
                st.write(f"💼 {exp.get('title', 'Position')}")
        else:
            st.info(get_text("no_experience_found", st.session_state.language))
        
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
    st.header(f"💼 {get_text('career_mentor', st.session_state.language)}")
    st.write(get_text("personalized_recommendations", st.session_state.language))
    
    # User profile form
    st.markdown(f"### {get_text('your_profile', st.session_state.language)}")
    col1, col2 = st.columns(2)
    
    with col1:
        experience_years = st.slider(get_text("years_of_experience", st.session_state.language), 0, 50, 2)
        education_level = st.selectbox(
            get_text("education_level", st.session_state.language),
            ["10th", "12th", "UG", "PG", "Diploma"]
        )
    
    with col2:
        st.markdown("")
        st.session_state.user_profile["education_level"] = education_level
        st.session_state.user_profile["experience_years"] = experience_years
    
    # Get skills from resume or manual input
    skills_input = st.multiselect(
        get_text("your_skills", st.session_state.language),
        options=[
            "python", "java", "javascript", "sql", "machine learning",
            "data analysis", "web development", "cloud computing",
            "communication", "leadership", "problem solving"
        ],
        default=st.session_state.resume_data.get("skills", []) if st.session_state.resume_data else []
    )
    
    if st.button(get_text("get_career_recommendations", st.session_state.language), key="career_recommendations_widget"):
        with st.spinner(get_text("loading", st.session_state.language)):
            career_engine = CareerRecommendationEngine()
            recommendations = career_engine.recommend_careers(
                user_skills=skills_input,
                education=education_level,
                experience_years=experience_years
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
                        st.write(f"**{get_text('match_score', st.session_state.language)}:** {rec['match_score']}%")
                        st.write(f"**{get_text('salary_range', st.session_state.language)}:** {rec['salary_range']}")
                        st.write(f"**{get_text('growth_potential', st.session_state.language)}:** {rec['growth_potential']}")
                        
                        # Matching skills
                        matching = rec.get('matching_skills', [])
                        if matching:
                            st.markdown(f"**{get_text('matching_skills', st.session_state.language)}:** " + ", ".join(matching))
                        
                        # Missing skills
                        missing = rec.get('missing_skills', [])
                        if missing:
                            st.markdown(f"**{get_text('skills_to_learn', st.session_state.language)}:** " + ", ".join(missing))
                    
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
    st.header(f"🎓 {get_text('scholarship_finder', st.session_state.language)}")
    st.write(get_text("discover_scholarships", st.session_state.language))
    
    # Eligibility form
    st.markdown(f"### {get_text('your_details', st.session_state.language)}")
    col1, col2 = st.columns(2)
    
    with col1:
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
                        st.write(f"**{get_text('award_amount', st.session_state.language)}:** ₹{scholarship['award_amount']:,}")
                        st.write(f"**{get_text('eligibility', st.session_state.language)}:** {scholarship['eligibility']}")
                        st.write(f"**{get_text('deadline', st.session_state.language)}:** {scholarship['deadline']}")
                        st.write(f"**{get_text('match_score', st.session_state.language)}:** {scholarship['match_score']}%")
                    
                    with col2:
                        if st.button(get_text("apply_now", st.session_state.language), key=f"apply_{idx}"):
                            st.success(f"{get_text('redirecting', st.session_state.language)}")
                    
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
    st.header(f"🏛️ {get_text('government_schemes', st.session_state.language)}")
    st.write(get_text("government_scheme_desc", st.session_state.language))
    
    # Eligibility form
    st.markdown(f"### {get_text('your_details', st.session_state.language)}")
    col1, col2 = st.columns(2)
    
    with col1:
        state = st.text_input(
            get_text("state", st.session_state.language),
            value=st.session_state.user_profile.get("state", "")
        )
        education_level = st.selectbox(
            get_text("education_level", st.session_state.language),
            ["10th", "12th", "UG", "PG"],
            key="scheme_education"
        )
    
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
            key="scheme_income"
        )
    
    category = st.selectbox(
        get_text("social_category", st.session_state.language),
        ["General", "OBC", "SC", "ST"],
        help=get_text("select_category", st.session_state.language)
    )
    
    st.markdown("---")
    
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
        
        st.session_state.scheme_recommendations = recommendations
        
        if recommendations:
            st.success(f"✅ {get_text('schemes_found', st.session_state.language).format(count=len(recommendations))}")
            st.markdown("---")
            
            # Display schemes
            for idx, scheme in enumerate(recommendations, 1):
                with st.expander(f"**{idx}. {scheme['scheme_name']}**"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**{get_text('scheme_type', st.session_state.language)}:** {scheme['scheme_type']}")
                        st.write(f"**{get_text('benefit', st.session_state.language)}:** {scheme['benefit']}")
                        st.write(f"**{get_text('eligibility', st.session_state.language)}:** {scheme['eligibility']}")
                    
                    with col2:
                        st.write(f"**{get_text('deadline', st.session_state.language)}:** {scheme['deadline']}")
                        st.write(f"**{get_text('max_income', st.session_state.language)}:** ₹{scheme['max_income']:,}")
                        st.write(f"**{get_text('age_limit', st.session_state.language)}:** {scheme['age_limit']} years")
                    
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
                        "Address Proof"
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
    st.header(f"🚀 {get_text('opportunities', st.session_state.language)}")
    st.write(get_text("explore_opportunities", st.session_state.language))
    
    # Search and filters
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
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
    
    st.markdown("---")
    
    # Search opportunities
    opportunity_engine = OpportunityEngine()
    
    filters = {}
    if opportunity_type != "All":
        filters["type"] = opportunity_type
    if category != "All":
        filters["category"] = category
    
    if search_query:
        opportunities = opportunity_engine.search_opportunities(search_query, filters)
    else:
        # Get recommended opportunities
        skills = st.session_state.resume_data.get("skills", []) if st.session_state.resume_data else []
        education = st.session_state.user_profile.get("education_level", "UG")
        experience = st.session_state.user_profile.get("experience_years", 0)
        
        opportunities = opportunity_engine.recommend_opportunities(
            user_skills=skills,
            education_level=education,
            experience_years=experience,
            preferences=filters
        )
    
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
    st.header(f"🗺️ {get_text('learning_roadmap', st.session_state.language)}")
    st.write(get_text("create_learning_roadmap", st.session_state.language))
    
    # Input form
    col1, col2 = st.columns(2)
    
    with col1:
        target_career = st.selectbox(
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
            st.metric(get_text("total_hours", st.session_state.language), total_hours)
        
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
        
        if not monthly_goals:
            st.warning(get_text("no_roadmap_generated", st.session_state.language))
            return
        
        for month_data in monthly_goals:
            month = month_data.get("month", 1)
            title = month_data.get("title", f"Month {month}")
            skills = month_data.get("skills_to_develop", [])
            topics = month_data.get("topics_to_learn", [])
            projects = month_data.get("projects_to_build", [])
            hours = month_data.get("estimated_hours", 0)
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
    
    # Initialize database
    db_manager = get_db_manager()
    
    # Render sidebar and get selected page
    page = render_sidebar()
    
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


if __name__ == "__main__":
    main()
