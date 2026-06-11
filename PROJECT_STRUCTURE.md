# Project Structure

## Career Bridge AI - Comprehensive Project Layout

---

## Directory Tree Overview

```
career-bridge-ai/
│
├── 📄 Configuration & Documentation Files
│   ├── README.md                    # Main project documentation
│   ├── AGENTS.md                    # AI agents specification
│   ├── ARCHITECTURE.md              # System architecture
│   ├── ROADMAP.md                   # Development roadmap
│   ├── CONTRIBUTING.md              # Contribution guidelines
│   ├── CODE_OF_CONDUCT.md           # Community guidelines
│   ├── SECURITY.md                  # Security policy
│   ├── CHANGELOG.md                 # Version history
│   ├── USER_MANUAL.md               # User documentation
│   ├── PROJECT_STRUCTURE.md         # This file
│   ├── LICENSE                      # AGPL-3.0 License
│   ├── .env.example                 # Environment template
│   ├── .gitignore                   # Git ignore rules
│   ├── .editorconfig                # Editor configuration
│   ├── requirements.txt             # Python dependencies
│   └── requirements-dev.txt         # Development dependencies
│
├── 📁 Source Code (src/)
│   ├── __init__.py                  # Package initialization
│   ├── main.py                      # Application entry point
│   ├── config.py                    # Configuration management
│   │
│   ├── agents/                      # AI Agents
│   │   ├── __init__.py
│   │   ├── base_agent.py            # Base agent class
│   │   ├── resume_analyzer.py       # Resume Analysis Agent
│   │   ├── career_recommender.py    # Career Recommendation Agent
│   │   ├── scholarship_matcher.py   # Scholarship Matching Agent
│   │   ├── govt_scheme_agent.py     # Government Scheme Agent
│   │   ├── opportunity_discovery.py # Opportunity Discovery Agent
│   │   └── learning_roadmap.py      # Learning Roadmap Agent
│   │
│   ├── models/                      # ML/AI Models
│   │   ├── __init__.py
│   │   ├── nlp_processor.py         # NLP pipeline
│   │   ├── skill_extractor.py       # Skill extraction model
│   │   ├── matching_engine.py       # Matching algorithms
│   │   ├── ats_calculator.py        # ATS score calculation
│   │   └── embeddings.py            # Embedding generation
│   │
│   ├── database/                    # Database Operations
│   │   ├── __init__.py
│   │   ├── connection.py            # Database connection
│   │   ├── models.py                # Database schema
│   │   ├── queries.py               # Database queries
│   │   ├── migrations/              # Database migrations
│   │   │   └── __init__.py
│   │   └── seeds.py                 # Seed data
│   │
│   ├── utils/                       # Utility Functions
│   │   ├── __init__.py
│   │   ├── pdf_parser.py            # PDF extraction
│   │   ├── docx_parser.py           # DOCX extraction
│   │   ├── text_processor.py        # Text processing
│   │   ├── validators.py            # Input validation
│   │   ├── formatters.py            # Output formatting
│   │   ├── constants.py             # Application constants
│   │   ├── logger.py                # Logging setup
│   │   └── exceptions.py            # Custom exceptions
│   │
│   ├── api/                         # API Endpoints (Future)
│   │   ├── __init__.py
│   │   ├── routes.py                # API routes
│   │   └── middleware.py            # API middleware
│   │
│   └── services/                    # Business Logic Services
│       ├── __init__.py
│       ├── resume_service.py        # Resume operations
│       ├── career_service.py        # Career operations
│       ├── scholarship_service.py   # Scholarship operations
│       ├── scheme_service.py        # Scheme operations
│       ├── opportunity_service.py   # Opportunity operations
│       └── learning_service.py      # Learning operations
│
├── 📁 Pages (pages/)                # Streamlit pages
│   ├── __init__.py
│   ├── 1_Resume_Analysis.py         # Resume analysis page
│   ├── 2_Career_Recommendations.py  # Career recommendation page
│   ├── 3_Scholarships.py            # Scholarship discovery page
│   ├── 4_Government_Schemes.py      # Government schemes page
│   ├── 5_Opportunities.py           # Opportunity dashboard
│   └── 6_Learning_Roadmap.py        # Learning roadmap page
│
├── 📁 Data (data/)                  # Data storage
│   ├── scholarships/                # Scholarship databases
│   │   ├── scholarships.json        # Main scholarship data
│   │   ├── national/                # National scholarships
│   │   ├── state/                   # State-specific scholarships
│   │   └── merit-based/             # Merit-based scholarships
│   │
│   ├── schemes/                     # Government schemes
│   │   ├── skill_development/       # Skill development schemes
│   │   ├── internship_programs/     # Internship programs
│   │   ├── education_support/       # Education support schemes
│   │   └── employment/              # Employment schemes
│   │
│   ├── opportunities/               # Opportunity data
│   │   ├── internships.json         # Internship listings
│   │   ├── hackathons.json          # Hackathon events
│   │   ├── competitions.json        # Competitions
│   │   ├── workshops.json           # Workshop listings
│   │   └── webinars.json            # Webinar schedules
│   │
│   ├── jobs/                        # Job profiles
│   │   ├── job_roles.json           # Job role database
│   │   ├── skills_taxonomy.json     # Skills hierarchy
│   │   └── industries.json          # Industry data
│   │
│   ├── courses/                     # Learning courses
│   │   ├── free_courses.json        # Free online courses
│   │   ├── paid_courses.json        # Paid courses
│   │   └── projects.json            # Project templates
│   │
│   ├── sample_data/                 # Sample data for testing
│   │   ├── sample_resumes/          # Sample resume files
│   │   └── test_data.json           # Test data
│   │
│   ├── career_bridge.db             # SQLite database file
│   └── backups/                     # Database backups
│
├── 📁 Documentation (docs/)         # Detailed documentation
│   ├── API_REFERENCE.md             # API documentation
│   ├── DATABASE_SCHEMA.md           # Database structure
│   ├── TESTING_GUIDE.md             # Testing procedures
│   ├── DEPLOYMENT.md                # Deployment guide
│   ├── TROUBLESHOOTING.md           # Troubleshooting guide
│   ├── ARCHITECTURE_DEEP_DIVE.md    # Detailed architecture
│   ├── AGENTS_DETAILED.md           # Detailed agent specs
│   ├── ML_MODELS.md                 # ML model documentation
│   └── CONTRIBUTING_DETAILED.md     # Detailed contribution guide
│
├── 📁 Uploads (uploads/)            # User file uploads
│   ├── resumes/                     # Uploaded resumes (temp)
│   ├── documents/                   # Supporting documents
│   └── .gitkeep                     # Keep directory in git
│
├── 📁 Models (models/)              # Pre-trained models
│   ├── spacy_models/                # spaCy language models
│   │   └── en_core_web_sm/          # English language model
│   │
│   ├── sentence_transformers/       # Sentence embeddings
│   │   ├── all-MiniLM-L6-v2/        # Embedding model
│   │   └── multi-qa-MiniLM-L6-cos-v1/  # QA embeddings
│   │
│   ├── classifiers/                 # Trained classifiers
│   │   ├── ats_scorer.pkl           # ATS scoring model
│   │   ├── skill_classifier.pkl     # Skill classifier
│   │   ├── career_predictor.pkl     # Career recommendation model
│   │   └── scholarship_matcher.pkl  # Scholarship matching model
│   │
│   ├── vectorizers/                 # Vectorizers
│   │   └── tfidf_vectorizer.pkl     # TF-IDF vectorizer
│   │
│   ├── metadata.json                # Model metadata
│   └── README.md                    # Model documentation
│
├── 📁 Tests (tests/)                # Test suite
│   ├── __init__.py
│   ├── conftest.py                  # Pytest configuration
│   ├── test_requirements.txt        # Test dependencies
│   │
│   ├── unit/                        # Unit tests
│   │   ├── test_resume_analyzer.py
│   │   ├── test_career_recommender.py
│   │   ├── test_scholarship_matcher.py
│   │   ├── test_scheme_agent.py
│   │   ├── test_opportunity_discovery.py
│   │   ├── test_learning_roadmap.py
│   │   ├── test_nlp_processor.py
│   │   ├── test_database.py
│   │   └── test_utils.py
│   │
│   ├── integration/                 # Integration tests
│   │   ├── test_agent_integration.py
│   │   ├── test_api_integration.py
│   │   └── test_database_integration.py
│   │
│   ├── fixtures/                    # Test fixtures
│   │   ├── sample_resumes/          # Sample resume files
│   │   ├── mock_data.py             # Mock data
│   │   └── fixtures.json            # Test fixtures
│   │
│   └── performance/                 # Performance tests
│       └── test_performance.py
│
├── 📁 Scripts (scripts/)            # Utility scripts
│   ├── init_db.py                   # Database initialization
│   ├── seed_data.py                 # Load seed data
│   ├── train_models.py              # Train ML models
│   ├── download_models.py           # Download ML models
│   ├── backup_db.py                 # Backup database
│   ├── migrate_db.py                # Database migration
│   ├── update_opportunities.py      # Update opportunity data
│   ├── generate_embeddings.py       # Generate embeddings
│   └── maintenance.py               # Maintenance tasks
│
├── 📁 Assets (assets/)              # Static assets
│   ├── images/                      # Images
│   │   ├── logo.png
│   │   ├── banner.png
│   │   └── icons/
│   │
│   ├── css/                         # Stylesheets (future)
│   │   └── custom.css
│   │
│   ├── js/                          # JavaScript (future)
│   │   └── custom.js
│   │
│   └── fonts/                       # Custom fonts
│
├── 📁 Logs (logs/)                  # Application logs
│   ├── app.log                      # Main application log
│   ├── error.log                    # Error log
│   ├── debug.log                    # Debug log
│   └── .gitkeep                     # Keep directory in git
│
├── 📁 GitHub (. github/)            # GitHub configuration
│   ├── workflows/                   # GitHub Actions
│   │   ├── ci.yml                   # CI/CD pipeline
│   │   ├── tests.yml                # Test pipeline
│   │   └── deploy.yml               # Deployment pipeline
│   │
│   ├── ISSUE_TEMPLATE/              # Issue templates
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── question.md
│   │
│   └── PULL_REQUEST_TEMPLATE.md     # PR template
│
└── 📁 Environment & Config
    ├── .env.example                 # Environment template
    ├── .env                         # Environment variables (not in git)
    ├── .gitignore                   # Git ignore rules
    ├── .editorconfig                # Editor configuration
    ├── .pylintrc                    # Pylint configuration
    ├── .flake8                      # Flake8 configuration
    └── pytest.ini                   # Pytest configuration
```

---

## File Purpose Guide

### Configuration Files

| File | Purpose |
|------|---------|
| `.env.example` | Template for environment variables |
| `.env` | Actual environment variables (local only) |
| `.gitignore` | Files to exclude from Git |
| `.editorconfig` | Editor settings standardization |
| `requirements.txt` | Production dependencies |
| `requirements-dev.txt` | Development dependencies |
| `pytest.ini` | Pytest configuration |
| `.pylintrc` | Code linting configuration |

### Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Main project overview |
| `AGENTS.md` | AI agent specifications |
| `ARCHITECTURE.md` | System architecture |
| `ROADMAP.md` | Development roadmap |
| `CONTRIBUTING.md` | Contribution guidelines |
| `CODE_OF_CONDUCT.md` | Community standards |
| `SECURITY.md` | Security policy |
| `CHANGELOG.md` | Version history |
| `USER_MANUAL.md` | User documentation |
| `PROJECT_STRUCTURE.md` | Project layout |
| `LICENSE` | Legal license |

### Source Code Structure

| Directory | Purpose |
|-----------|---------|
| `src/agents/` | AI agents implementation |
| `src/models/` | ML/AI models |
| `src/database/` | Database operations |
| `src/utils/` | Utility functions |
| `src/api/` | API endpoints |
| `src/services/` | Business logic |
| `pages/` | Streamlit UI pages |

### Data Directory

| Subdirectory | Purpose |
|--------------|---------|
| `data/scholarships/` | Scholarship databases |
| `data/schemes/` | Government schemes |
| `data/opportunities/` | Opportunities data |
| `data/jobs/` | Job profiles & skills |
| `data/courses/` | Course information |
| `data/sample_data/` | Test data |

### Development Directories

| Directory | Purpose |
|-----------|---------|
| `tests/` | Test suite |
| `scripts/` | Utility scripts |
| `models/` | ML models |
| `uploads/` | User uploads |
| `logs/` | Application logs |
| `assets/` | Static assets |
| `docs/` | Detailed documentation |

---

## Key Directories Explained

### 1. src/agents/

**Purpose**: Core AI agent implementations

**Contents**:
- Base agent class for inheritance
- Resume Analysis Agent
- Career Recommendation Agent
- Scholarship Matching Agent
- Government Scheme Agent
- Opportunity Discovery Agent
- Learning Roadmap Agent

**Usage**: Import from `src.agents` in application code

### 2. src/models/

**Purpose**: ML and NLP model implementations

**Contents**:
- NLP processing pipeline
- Skill extraction model
- Matching engines
- ATS calculation
- Embedding generation

**Usage**: Used by agents for processing

### 3. src/database/

**Purpose**: Database operations and schema

**Contents**:
- Database connection management
- SQLite schema definitions
- Query functions
- Database migrations
- Seed data

**Usage**: Central data access layer

### 4. data/

**Purpose**: Data storage and databases

**Contents**:
- Scholarship and scheme databases
- Opportunity listings
- Job role and skill taxonomies
- Course recommendations
- SQLite database file

**Note**: Some files are JSON, others are database tables

### 5. tests/

**Purpose**: Test suite for quality assurance

**Contents**:
- Unit tests for each module
- Integration tests
- Test fixtures and mocks
- Performance tests

**Usage**: Run with `pytest tests/`

### 6. scripts/

**Purpose**: Utility and maintenance scripts

**Contents**:
- Database initialization
- Data seeding
- Model training
- Database backups
- Data updates

**Usage**: Run manually or via CI/CD

### 7. models/

**Purpose**: Pre-trained ML models storage

**Contents**:
- spaCy language models
- Sentence Transformer embeddings
- Trained classifiers
- Vectorizers

**Note**: Large files, not in repository (download on first run)

---

## Development Workflow

### Adding a New Feature

1. **Create branch**: `feature/feature-name`
2. **Add code**:
   - Implementation in `src/`
   - Tests in `tests/`
   - Documentation in docstrings
3. **Update docs**: Update README or relevant docs
4. **Run tests**: `pytest tests/`
5. **Commit & push**: Push to GitHub
6. **Create PR**: Open pull request

### File Organization Best Practices

1. **Keep files focused**: One responsibility per file
2. **Organize by feature**: Group related code
3. **Use packages**: Create `__init__.py` files
4. **Document thoroughly**: Add docstrings and comments
5. **Test coverage**: Write tests for new code
6. **Configuration**: Use `.env` for configuration

---

## Database Files

### SQLite Database

**Location**: `data/career_bridge.db`

**Tables**:
- Users
- Resumes
- Skills
- Careers
- Scholarships
- Schemes
- Opportunities
- Applications
- Learning Paths

### Backup & Recovery

- Backups stored in: `data/backups/`
- Create backup: `python scripts/backup_db.py`
- Restore backup: `python scripts/restore_db.py`

---

## Ignored Files & Directories

**Not tracked in Git** (.gitignore):
- `venv/` - Virtual environment
- `.env` - Environment variables
- `__pycache__/` - Python cache
- `*.pyc` - Compiled Python
- `*.pyo` - Optimized Python
- `.DS_Store` - macOS files
- `uploads/` - User uploads
- `logs/` - Application logs
- `*.egg-info/` - Package info

---

## Import Examples

### Importing from src/

```python
# Import agent
from src.agents.resume_analyzer import ResumeAnalyzer

# Import model
from src.models.nlp_processor import NLPProcessor

# Import database
from src.database.connection import get_db

# Import utils
from src.utils.validators import validate_email

# Import services
from src.services.resume_service import ResumeService
```

### Importing from pages/

```python
# In Streamlit app
from pages.resume_analysis import show_resume_analysis
```

---

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run src/main.py

# Run tests
pytest tests/

# Check code coverage
pytest tests/ --cov=src

# Run specific test
pytest tests/unit/test_resume_analyzer.py

# Lint code
pylint src/

# Format code
black src/

# Initialize database
python scripts/init_db.py

# Seed data
python scripts/seed_data.py
```

---

## Size & Performance Notes

- **Database**: Grows with user data
- **Models**: ~1-2GB for all models
- **Uploads**: Temporary files, cleaned regularly
- **Logs**: Rotated, ~1-10MB typical

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-06-11 | Initial project structure |

---

**Last Updated**: 2026-06-11  
**Structure Version**: 1.0.0

For questions about file organization, see [README.md](README.md) or [CONTRIBUTING.md](CONTRIBUTING.md)
