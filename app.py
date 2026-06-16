"""
Career Bridge AI - Main Streamlit Application

A comprehensive AI-powered student career guidance platform providing
resume analysis, career recommendations, scholarship finder, government
scheme recommendations, opportunity discovery, and learning roadmaps.
"""

import logging
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from config import STREAMLIT_PAGE_TITLE, STREAMLIT_PAGE_ICON, STREAMLIT_LAYOUT, ensure_directories
from database import get_db_manager
from career_engine import CareerRecommendationEngine
from opportunity_engine import OpportunityEngine
from resume_parser import ResumeParser
from roadmap_engine import RoadmapGenerator
from scholarship_engine import ScholarshipRecommendationEngine
from scheme_engine import GovernmentSchemeEngine
from services.ai_provider import (
    DEFAULT_BYOK_ENDPOINT,
    DEFAULT_BYOK_MODEL,
    DEFAULT_OLLAMA_MODEL,
    OLLAMA_GENERATE_URL,
    AIProviderConfig,
    generate_ai_response,
)
from services.language import get_language_names, normalize_language, translate

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

    TODO: Implement session state initialization for:
        - User profile
        - Uploaded files
        - Recommendations
        - Learning plans
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

    if "ai_assistant_response" not in st.session_state:
        st.session_state.ai_assistant_response = ""

    if "ai_assistant_warning" not in st.session_state:
        st.session_state.ai_assistant_warning = False

    if "language" not in st.session_state:
        st.session_state.language = normalize_language(
            st.session_state.get("selected_language") or os.getenv("DEFAULT_LANGUAGE", "English")
        )
    else:
        st.session_state.language = normalize_language(st.session_state.language)

    # Keep the older key in sync for existing AI/language code paths.
    st.session_state.selected_language = st.session_state.language

    if "language_selector" not in st.session_state:
        st.session_state.language_selector = st.session_state.language


def render_sidebar() -> str:
    """
    Render sidebar navigation.

    Returns:
        Selected page name.

    TODO: Implement sidebar with page navigation links.
    """
    st.sidebar.title("Career Bridge AI")
    st.sidebar.write("Your Personal Career Guidance Platform")
    st.sidebar.divider()

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

        default_language = normalize_language(os.getenv("DEFAULT_LANGUAGE", "English"))
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
    st.title("🎓 Career Bridge AI")
    st.write("Welcome to Career Bridge AI - Your Personal Career Guidance Platform")

    st.markdown("""
    ## Bridging Students to Opportunities
    
    Career Bridge AI is an intelligent platform that helps you navigate your career journey with:
    """)

    # Feature cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "📄 **Resume Analyzer**\nGet AI-powered analysis of your resume with ATS scoring and improvement suggestions."
        )

    with col2:
        st.success(
            "💼 **Career Recommendations**\nDiscover career paths that match your skills and experience with detailed guidance."
        )

    with col3:
        st.warning("🎓 **Scholarship Finder**\nFind and apply for scholarships matching your eligibility criteria.")

    st.markdown("---")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.info("🏛️ **Government Schemes**\nAccess information about government schemes and assistance programs.")

    with col5:
        st.success("🚀 **Opportunities**\nExplore internships, competitions, and career-building opportunities.")

    with col6:
        st.warning("🗺️ **Learning Roadmap**\nCreate personalized learning paths to bridge your skill gaps.")

    st.markdown("---")

    # Quick statistics
    st.markdown("## Platform Statistics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Active Users", "10,000+", "+15%")

    with col2:
        st.metric("Opportunities", "5,000+", "+20%")

    with col3:
        st.metric("Scholarships", "1,500+", "+10%")

    with col4:
        st.metric("Success Rate", "85%", "+5%")

    st.markdown("---")

    # Getting started
    st.markdown("## Getting Started")
    st.markdown("""
    1. **Upload Your Resume** - Start with resume analysis to extract your skills
    2. **Get Career Recommendations** - Discover careers that match your profile
    3. **Find Scholarships** - Search and apply for scholarships
    4. **Explore Opportunities** - Find internships and competitions
    5. **Create Learning Plan** - Build your personalized learning roadmap
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
    st.header("📄 Resume Analyzer")
    st.write("Upload your resume for analysis")

    # File upload
    uploaded_file = st.file_uploader("Upload your resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        # Save uploaded file
        file_path = Path("uploads") / uploaded_file.name
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Parse resume
        parser = ResumeParser(file_path)

        if not parser.validate_resume():
            st.error("Could not extract text from the resume. Please upload a readable PDF/DOCX.")
            return

        # Extract information
        with st.spinner("Analyzing your resume..."):
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
        st.success("✅ Resume analyzed successfully!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("ATS Score", f"{ats_score:.1f}/100", delta="Good" if ats_score > 70 else "Needs Improvement")

        with col2:
            st.metric("Skills Found", len(skills), delta=f"+{len(skills)}")

        with col3:
            st.metric("Education", len(education), delta="Complete" if education else "Missing")

        st.markdown("---")

        # Skills section
        st.markdown("## Extracted Skills")
        if skills:
            cols = st.columns(4)
            for idx, skill in enumerate(skills):
                with cols[idx % 4]:
                    st.label_option_text(skill)
        else:
            st.info("No skills detected. Please ensure your resume contains your skills.")

        st.markdown("---")

        # Education section
        st.markdown("## Education")
        if education:
            for edu in education:
                st.write(f"📚 {edu.get('type', 'Degree')}")
        else:
            st.info("No education information found.")

        st.markdown("---")

        # Experience section
        st.markdown("## Work Experience")
        if experience:
            for exp in experience:
                st.write(f"💼 {exp.get('title', 'Position')}")
        else:
            st.info("No work experience found.")

        st.markdown("---")

        # Improvement suggestions
        st.markdown("## Improvement Suggestions")
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
            st.success("Great job! Your resume looks good.")


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
    st.header("💼 Career Mentor")
    st.write("Get personalized career recommendations")

    # User profile form
    st.markdown("### Your Profile")
    col1, col2 = st.columns(2)

    with col1:
        experience_years = st.slider("Years of Experience", 0, 50, 2)
        education_level = st.selectbox("Education Level", ["10th", "12th", "UG", "PG", "Diploma"])

    with col2:
        st.markdown("")
        st.session_state.user_profile["education_level"] = education_level
        st.session_state.user_profile["experience_years"] = experience_years

    # Get skills from resume or manual input
    skills_input = st.multiselect(
        "Your Skills",
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
    st.session_state.user_profile["skills"] = skills_input

    if st.button("Get Career Recommendations", key="career_recommendations_widget"):
        with st.spinner("Generating career recommendations..."):
            career_engine = CareerRecommendationEngine()
            recommendations = career_engine.recommend_careers(
                user_skills=skills_input, education=education_level, experience_years=experience_years
            )

        st.session_state.career_recommendations_data = recommendations

        if recommendations:
            st.success(f"✅ Found {len(recommendations)} career recommendations!")
            st.markdown("---")

            # Display recommendations
            for idx, rec in enumerate(recommendations, 1):
                with st.container():
                    col1, col2 = st.columns([3, 1])

                    with col1:
                        st.markdown(f"### {idx}. {rec['career_name']}")
                        st.write(f"**Match Score:** {rec['match_score']}%")
                        st.write(f"**Salary Range:** {rec['salary_range']}")
                        st.write(f"**Growth Potential:** {rec['growth_potential']}")

                        # Matching skills
                        matching = rec.get("matching_skills", [])
                        if matching:
                            st.markdown("**Matching Skills:** " + ", ".join(matching))

                        # Missing skills
                        missing = rec.get("missing_skills", [])
                        if missing:
                            st.markdown("**Skills to Learn:** " + ", ".join(missing))

                    with col2:
                        if st.button("Learn More", key=f"career_{idx}"):
                            st.info(f"Career: {rec['career_name']}\n\nSkills: {', '.join(rec['required_skills'])}")

                    st.divider()
        else:
            st.info("No career recommendations found. Please add more skills to your profile.")


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
    st.header("🎓 Scholarship Finder")
    st.write("Discover scholarship opportunities")

    # Eligibility form
    st.markdown("### Your Details")
    col1, col2 = st.columns(2)

    with col1:
        education_level = st.selectbox("Education Level", ["10th", "12th", "UG", "PG"], key="scholarship_education")
        state = st.text_input("State", value=st.session_state.user_profile.get("state", ""))

    with col2:
        annual_income = st.number_input(
            "Annual Family Income (₹)", min_value=0, value=st.session_state.user_profile.get("annual_income", 0)
        )
        gpa = st.number_input("GPA (if available)", min_value=0.0, max_value=4.0, value=3.5)

    st.markdown("---")

    if st.button("Find Scholarships", key="find_scholarships"):
        with st.spinner("Searching for scholarships..."):
            scholarship_engine = ScholarshipRecommendationEngine()
            recommendations = scholarship_engine.recommend_scholarships(
                education_level=education_level, state=state, annual_income=annual_income, gpa=gpa
            )

        st.session_state.scholarship_recommendations = recommendations

        if recommendations:
            st.success(f"✅ Found {len(recommendations)} matching scholarships!")
            st.markdown("---")

            # Display scholarships
            for idx, scholarship in enumerate(recommendations, 1):
                with st.container():
                    col1, col2 = st.columns([3, 1])

                    with col1:
                        st.markdown(f"### {idx}. {scholarship['scholarship_name']}")
                        st.write(f"**Award Amount:** ₹{scholarship['award_amount']:,}")
                        st.write(f"**Eligibility:** {scholarship['eligibility']}")
                        st.write(f"**Deadline:** {scholarship['deadline']}")
                        st.write(f"**Match Score:** {scholarship['match_score']}%")

                    with col2:
                        if st.button("Apply Now", key=f"apply_{idx}"):
                            st.success(f"Redirecting to {scholarship['scholarship_name']} application...")

                    st.divider()
        else:
            st.info("No scholarships found matching your criteria. Try adjusting your details.")


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
    st.header("🏛️ Government Scheme Recommender")
    st.write("Find relevant government schemes")

    # Eligibility form
    st.markdown("### Your Details")
    col1, col2 = st.columns(2)

    with col1:
        state = st.text_input("State", value=st.session_state.user_profile.get("state", ""))
        education_level = st.selectbox("Education Level", ["10th", "12th", "UG", "PG"], key="scheme_education")

    with col2:
        age = st.number_input("Age", min_value=1, max_value=100, value=20)
        annual_income = st.number_input(
            "Annual Family Income (₹)",
            min_value=0,
            value=st.session_state.user_profile.get("annual_income", 0),
            key="scheme_income",
        )

    category = st.selectbox(
        "Social Category", ["General", "OBC", "SC", "ST"], help="Select your social category for eligibility"
    )

    st.markdown("---")

    if st.button("Get Scheme Recommendations", key="get_schemes"):
        with st.spinner("Finding government schemes..."):
            scheme_engine = GovernmentSchemeEngine()
            recommendations = scheme_engine.recommend_schemes(
                state=state, education_level=education_level, annual_income=annual_income, age=age, category=category
            )

        st.session_state.scheme_recommendations = recommendations

        if recommendations:
            st.success(f"✅ Found {len(recommendations)} eligible government schemes!")
            st.markdown("---")

            # Display schemes
            for idx, scheme in enumerate(recommendations, 1):
                with st.expander(f"**{idx}. {scheme['scheme_name']}**"):
                    col1, col2 = st.columns(2)

                    with col1:
                        st.write(f"**Type:** {scheme['scheme_type']}")
                        st.write(f"**Benefit:** {scheme['benefit']}")
                        st.write(f"**Eligibility:** {scheme['eligibility']}")

                    with col2:
                        st.write(f"**Deadline:** {scheme['deadline']}")
                        st.write(f"**Max Income:** ₹{scheme['max_income']:,}")
                        st.write(f"**Age Limit:** {scheme['age_limit']} years")

                    # Application process
                    st.markdown("**Application Process:**")
                    st.markdown("""
                    1. Verify eligibility criteria
                    2. Gather required documents
                    3. Complete application form
                    4. Submit to government office
                    5. Track status
                    """)

                    # Required documents
                    st.markdown("**Required Documents:**")
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
            st.info("No government schemes found matching your criteria.")


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
    st.header("🚀 Opportunity Dashboard")
    st.write("Explore career opportunities")

    # Search and filters
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        search_query = st.text_input("Search opportunities", placeholder="e.g., internship, python, data science")

    with col2:
        opportunity_type = st.selectbox("Type", ["All", "internship", "bootcamp", "competition", "job"])

    with col3:
        category = st.selectbox("Category", ["All", "tech", "data", "business", "learning", "security"])

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
            user_skills=skills, education_level=education, experience_years=experience, preferences=filters
        )

    # Display opportunities
    if opportunities:
        st.success(f"Found {len(opportunities)} opportunities!")
        st.markdown("---")

        for idx, opp in enumerate(opportunities, 1):
            with st.container():
                col1, col2 = st.columns([3, 1])

                with col1:
                    st.markdown(f"### {idx}. {opp.get('opportunity_name', 'Opportunity')}")

                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        st.write(f"**Type:** {opp.get('opportunity_type', 'N/A')}")
                    with col_b:
                        st.write(f"**Category:** {opp.get('category', 'N/A')}")
                    with col_c:
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

                st.divider()
    else:
        st.info("No opportunities found. Try adjusting your filters or search query.")


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
    st.header("🗺️ Learning Roadmap Generator")
    st.write("Create your personalized learning roadmap")

    # Input form
    col1, col2 = st.columns(2)

    with col1:
        target_career = st.selectbox(
            "Target Career",
            ["Data Scientist", "Software Developer", "DevOps Engineer", "Full Stack Developer", "ML Engineer"],
        )
        available_hours = st.slider("Available Hours per Week", min_value=5, max_value=40, value=15, step=5)

    with col2:
        duration_months = st.slider("Learning Duration (months)", min_value=1, max_value=24, value=6)
        st.selectbox("Preferred Pace", ["Beginner", "Intermediate", "Advanced"])

    st.markdown("---")

    if st.button("Generate Learning Roadmap", key="generate_roadmap"):
        with st.spinner("Creating your personalized roadmap..."):
            roadmap_engine = RoadmapGenerator()

            # Get current skills
            current_skills = st.session_state.resume_data.get("skills", []) if st.session_state.resume_data else []

            # Generate plan
            learning_plan = roadmap_engine.generate_learning_plan(
                current_skills=current_skills,
                target_career=target_career,
                available_hours_per_week=available_hours,
                duration_months=duration_months,
            )

        st.session_state.learning_plan = learning_plan

        st.success("✅ Roadmap generated successfully!")
        st.markdown("---")

        # Display learning plan summary
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Target Career", target_career)
        with col2:
            st.metric("Duration", f"{duration_months} months")
        with col3:
            st.metric("Weekly Hours", f"{available_hours} hrs")
        with col4:
            total_hours = available_hours * 4 * duration_months
            st.metric("Total Hours", total_hours)

        st.markdown("---")

        # Skill gap analysis
        st.markdown("## Skill Gap Analysis")
        current = learning_plan.get("current_skills", [])
        target = learning_plan.get("target_skills", [])
        missing = learning_plan.get("missing_skills", [])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"**Current Skills:** {len(current)}")
            for skill in current:
                st.write(f"✅ {skill}")

        with col2:
            st.write(f"**Target Skills:** {len(target)}")
            for skill in target:
                st.write(f"🎯 {skill}")

        with col3:
            st.write(f"**Skills to Learn:** {len(missing)}")
            for skill in missing:
                st.write(f"📚 {skill}")

        st.markdown("---")

        # Monthly breakdown
        st.markdown("## Monthly Breakdown")
        monthly_goals = learning_plan.get("monthly_goals", [])

        for month_data in monthly_goals:
            month = month_data.get("month", 1)
            skills = month_data.get("skills_to_develop", [])
            hours = month_data.get("estimated_hours", 0)

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

        st.markdown("---")

        # Action buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Download Roadmap (PDF)", key="download_roadmap"):
                st.success("Roadmap downloaded!")

        with col2:
            if st.button("Start Learning", key="start_learning"):
                st.success("Start with the first month's goals!")

        with col3:
            if st.button("Share Roadmap", key="share_roadmap"):
                st.success("Share link copied to clipboard!")


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
            ["Local Ollama", "BYOK", "Rule-based fallback"],
            horizontal=True,
            help="Use local Ollama, your own API key/token, or an offline fallback response.",
        )

        col1, col2 = st.columns(2)
        with col1:
            if provider == "BYOK":
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
            if provider == "BYOK":
                byok_endpoint = st.text_input(
                    "BYOK API endpoint",
                    value=get_runtime_setting("BYOK_API_URL", DEFAULT_BYOK_ENDPOINT),
                    help="OpenAI-compatible chat completions endpoint.",
                )
            else:
                byok_endpoint = DEFAULT_BYOK_ENDPOINT
                st.text_input(
                    "Ollama API URL",
                    value=get_runtime_setting("OLLAMA_API_URL", OLLAMA_GENERATE_URL),
                    key="ollama_url_input",
                    help="Local Ollama generate endpoint.",
                )

        if provider == "BYOK":
            api_token = st.text_input(
                "API key/token",
                value=get_runtime_setting("BYOK_API_KEY", ""),
                type="password",
                help="Your token is used only for this Streamlit session and is not saved in the repository.",
            )
            ollama_url = OLLAMA_GENERATE_URL
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


def main() -> None:
    """
    Main application entry point.

    Orchestrates page routing and application flow.
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
        else:
            render_home_page()
    except Exception as exc:
        logger.exception("Page failed to render: %s", exc)
        st.error("This page could not load right now.")
        st.warning("Please try again or use another feature. The rest of Career Bridge AI is still available.")


if __name__ == "__main__":
    main()
