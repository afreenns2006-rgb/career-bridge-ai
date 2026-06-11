# Career Bridge AI - System Architecture

## Comprehensive Architecture Documentation

---

## Table of Contents

1. [Overview](#overview)
2. [System Components](#system-components)
3. [Frontend Layer](#frontend-layer)
4. [Backend Layer](#backend-layer)
5. [Database Layer](#database-layer)
6. [AI/ML Layer](#aiml-layer)
7. [Data Flow](#data-flow)
8. [Technology Stack](#technology-stack)
9. [Scalability & Performance](#scalability--performance)
10. [Security Architecture](#security-architecture)
11. [Deployment Architecture](#deployment-architecture)

---

## Overview

Career Bridge AI follows a **multi-layered architecture** with clear separation of concerns:

```
┌─────────────────────────────────────────────────────┐
│            User Interface Layer (Streamlit)         │
├─────────────────────────────────────────────────────┤
│            API & Business Logic Layer               │
├─────────────────────────────────────────────────────┤
│            AI/ML Processing Layer                   │
├─────────────────────────────────────────────────────┤
│            Data Access Layer (Database)             │
├─────────────────────────────────────────────────────┤
│            Storage Layer (Files & DB)               │
└─────────────────────────────────────────────────────┘
```

---

## System Components

### Core Components

1. **Frontend** - User-facing interface
2. **Backend** - Business logic and processing
3. **AI/ML Engine** - Machine learning and NLP
4. **Database** - Data persistence
5. **External Services** - Third-party integrations (future)

### Agent System

```
┌─────────────────────────────────────┐
│     Agent Orchestration Layer       │
└─────────────────────────────────────┘
         ↓           ↓          ↓
    ┌────────┐  ┌────────┐  ┌────────┐
    │ Resume │  │Career  │  │Scholar-│
    │Analysis│  │Recommend│ │  ship  │
    │ Agent  │  │ Agent  │  │Matcher │
    └────────┘  └────────┘  └────────┘
         ↓           ↓          ↓
    ┌─────────────────────────────┐
    │  Shared Model Layer         │
    │  - NLP Pipeline             │
    │  - Skill Extractor          │
    │  - Matching Engine          │
    └─────────────────────────────┘
```

---

## Frontend Layer

### Technology: Streamlit

**Architecture**:
```
Streamlit App
├── pages/
│   ├── Resume_Analysis.py
│   ├── Career_Recommendations.py
│   ├── Scholarships.py
│   ├── Government_Schemes.py
│   ├── Opportunities.py
│   └── Learning_Roadmap.py
├── components/
│   ├── Header
│   ├── Sidebar Navigation
│   ├── Dashboard
│   └── Forms
└── state/
    └── Session management
```

### Key Pages

1. **Home Dashboard**
   - User overview
   - Quick actions
   - Notifications

2. **Resume Analysis**
   - Resume upload
   - Analysis results
   - Improvement suggestions

3. **Career Recommendations**
   - Career matches
   - Role details
   - Skill comparison

4. **Scholarship Discovery**
   - Scholarship search
   - Matching recommendations
   - Application tracking

5. **Government Schemes**
   - Scheme discovery
   - Eligibility checking
   - Application process

6. **Opportunity Dashboard**
   - Opportunity listings
   - Application tracker
   - Deadline alerts

7. **Learning Roadmap**
   - Custom roadmaps
   - Course recommendations
   - Progress tracking

### State Management

```python
# Streamlit session state
st.session_state.user_id
st.session_state.current_resume
st.session_state.selected_career
st.session_state.saved_opportunities
```

### UI Components

- File uploaders
- Data tables
- Charts and visualizations
- Forms and inputs
- Progress indicators
- Notifications

---

## Backend Layer

### Architecture

```
Backend Services
├── Services
│   ├── ResumeService
│   ├── CareerService
│   ├── ScholarshipService
│   ├── SchemeService
│   ├── OpportunityService
│   └── LearningService
│
├── Agents
│   ├── ResumeAnalysisAgent
│   ├── CareerRecommendationAgent
│   ├── ScholarshipMatchingAgent
│   ├── GovernmentSchemeAgent
│   ├── OpportunityDiscoveryAgent
│   └── LearningRoadmapAgent
│
└── Models/Processors
    ├── NLPProcessor
    ├── SkillExtractor
    ├── MatchingEngine
    └── ATSCalculator
```

### Service Layer

**Purpose**: Business logic and orchestration

```python
class ResumeService:
    def upload_resume(resume_file) -> Resume
    def analyze_resume(resume_id) -> Analysis
    def extract_skills(resume_text) -> Skills
    def calculate_ats_score(resume) -> Score
    def get_improvements(resume) -> Suggestions
```

### Agent Layer

**Purpose**: Specialized AI processing

Each agent implements:
- `process()` - Main processing method
- `validate_input()` - Input validation
- `generate_output()` - Output generation
- `log_operations()` - Activity logging

---

## Database Layer

### Database: SQLite

**Design Principles**:
- Normalized schema
- Referential integrity
- Indexed lookups
- Transaction support

### Core Tables

```
Users
├── id (PK)
├── email (UNIQUE)
├── password_hash
├── profile
└── preferences

Resumes
├── id (PK)
├── user_id (FK)
├── file_path
├── upload_date
└── version

Skills
├── id (PK)
├── name (UNIQUE)
├── category
└── proficiency_levels

Careers
├── id (PK)
├── title
├── description
├── required_skills
└── salary_range

Scholarships
├── id (PK)
├── name
├── amount
├── eligibility_criteria
└── deadline

Opportunities
├── id (PK)
├── type (internship/hackathon/etc)
├── title
├── deadline
└── details

Applications
├── id (PK)
├── user_id (FK)
├── opportunity_id (FK)
├── status
└── applied_date
```

### Query Optimization

```
Indexes on:
- user_id (frequent filters)
- opportunity_type (fast lookups)
- deadline (sorting)
- status (filtering applications)
```

### Database Connections

```python
# Connection pooling
class DatabaseConnection:
    def __init__(self):
        self.connection = sqlite3.connect('career_bridge.db')
    
    def query(self, sql, params):
        return self.connection.execute(sql, params)
    
    def close(self):
        self.connection.close()
```

---

## AI/ML Layer

### NLP Processing Pipeline

```
Raw Text
    ↓
[Tokenization]
    ↓
[Lemmatization]
    ↓
[Entity Recognition]
    ↓
[Dependency Parsing]
    ↓
Structured Output
```

### Skill Extraction Pipeline

```
Resume Text
    ↓
[spaCy NER] → Identify entities
    ↓
[Skill Matcher] → Match against skill taxonomy
    ↓
[Vectorizer] → Create embeddings
    ↓
[Classifier] → Classify skill level
    ↓
Skills List with Categories & Levels
```

### Matching Engine

```
User Profile
    ↓
[Vector Embedding]
    ↓
[Similarity Search]
    ↓
[Ranking Algorithm]
    ↓
[Filter & Sort]
    ↓
Ranked Matches
```

### Models Used

1. **spaCy en_core_web_sm**
   - Tokenization
   - POS tagging
   - Entity recognition
   - Dependency parsing

2. **Sentence Transformers**
   - all-MiniLM-L6-v2 for embeddings
   - Semantic similarity matching
   - Dense vector representations

3. **Scikit-learn**
   - Classification models
   - Clustering algorithms
   - Feature extraction
   - Model evaluation

---

## Data Flow

### Resume Upload & Analysis Flow

```
1. User Upload Resume
        ↓
2. File Validation
   ├─ File type check
   ├─ File size check
   └─ Scan for malware
        ↓
3. Text Extraction
   ├─ PDF Parser
   ├─ DOCX Parser
   └─ TXT Parser
        ↓
4. Text Preprocessing
   ├─ Cleaning
   ├─ Normalization
   └─ Structuring
        ↓
5. NLP Processing
   ├─ Tokenization
   ├─ NER (Named Entity Recognition)
   └─ Dependency Parsing
        ↓
6. Information Extraction
   ├─ Contact Info
   ├─ Education
   ├─ Experience
   └─ Skills
        ↓
7. Analysis
   ├─ ATS Score Calculation
   ├─ Quality Assessment
   ├─ Skill Extraction
   └─ Recommendations
        ↓
8. Storage
   ├─ Save to Database
   ├─ Store File
   └─ Cache Results
        ↓
9. Display Results
   └─ Show to User
```

### Career Recommendation Flow

```
User Profile (from Resume)
        ↓
Extract Features
├─ Skills
├─ Education
├─ Experience
└─ Interests
        ↓
Feature Engineering
├─ Vectorization
├─ Embedding
└─ Normalization
        ↓
Similarity Matching
├─ Compare with Job Profiles
├─ Score Compatibility
└─ Rank Results
        ↓
Enrich with Market Data
├─ Add Salary Info
├─ Add Growth Potential
└─ Add Market Demand
        ↓
Filter & Personalize
├─ Apply Preferences
├─ Rank by Relevance
└─ Limit Results
        ↓
Display Recommendations
```

### Scholarship Matching Flow

```
User Profile
        ↓
Extract Attributes
├─ Education Level
├─ Category
├─ Income
├─ Skills
└─ Location
        ↓
Load Scholarship Database
        ↓
Eligibility Check
├─ Filter by requirements
├─ Verify conditions
└─ Calculate match score
        ↓
Ranking
├─ Sort by relevance
├─ Prioritize deadline
└─ Consider success probability
        ↓
Personalize
├─ Apply user preferences
├─ Consider past applications
└─ Avoid duplicates
        ↓
Display Results
└─ Show matched scholarships
```

---

## Technology Stack

### Frontend
- **Framework**: Streamlit 1.28+
- **Language**: Python 3.9+
- **Components**: Streamlit widgets

### Backend
- **Language**: Python 3.9+
- **API**: Streamlit callbacks
- **Database**: SQLite 3.40+

### AI/ML
- **NLP**: spaCy 3.7+
- **Embeddings**: Sentence Transformers 2.2+
- **ML**: Scikit-learn 1.3+
- **Text Processing**: NLTK, TextBlob

### Data Processing
- **Data Analysis**: Pandas 2.0+
- **Numerical**: NumPy 1.24+
- **PDF**: PyPDF 3.17+
- **Document**: python-docx 0.8.11+

### Development
- **Version Control**: Git 2.40+
- **Testing**: Pytest 7.4+
- **Linting**: Pylint, Flake8
- **Formatting**: Black, autopep8

---

## Scalability & Performance

### Performance Optimization

1. **Caching**
   - Cache NLP models in memory
   - Cache frequently accessed data
   - Use Streamlit's `@st.cache_data`

2. **Indexing**
   - Database indexes on frequently queried columns
   - Vector indexing for similarity search

3. **Batch Processing**
   - Process multiple resumes in batch
   - Vectorize opportunities in batches

4. **Lazy Loading**
   - Load data on demand
   - Progressive disclosure of information

### Scalability Roadmap

**Phase 1: Current (SQLite)**
- Single-instance deployment
- Suitable for 10,000+ users
- Local file storage

**Phase 2: Future (PostgreSQL)**
- Distributed database
- Connection pooling
- Replication support

**Phase 3: Future (Microservices)**
- Separate services for each agent
- Independent scaling
- Message queue for async processing

**Phase 4: Future (Cloud)**
- Cloud database (AWS RDS, Google Cloud SQL)
- Object storage (S3, GCS)
- CDN for static assets

---

## Security Architecture

### Authentication & Authorization

```
User Request
    ↓
[Auth Middleware]
├─ Validate token
├─ Check permissions
└─ Rate limiting
    ↓
[Process Request]
    ↓
[Response]
```

### Data Protection

1. **In Transit**
   - HTTPS/TLS encryption
   - Secure headers

2. **At Rest**
   - Encrypted database (future)
   - Encrypted file storage
   - Secure backups

3. **In Process**
   - Input validation
   - SQL injection prevention
   - XSS protection

### Access Control

```
Admin Level
├─ User management
├─ System configuration
└─ Data management

User Level
├─ Own resume
├─ Own applications
└─ Public opportunities

Anonymous
└─ Public information
```

---

## Deployment Architecture

### Local Development

```
Developer Machine
├─ Python virtual environment
├─ SQLite database
├─ Local file storage
└─ Streamlit dev server
```

### Production Deployment

```
Web Server
├─ Nginx/Apache
├─ Streamlit app
└─ Gunicorn WSGI

Application Server
├─ Python runtime
├─ Dependencies
└─ Configuration

Database Server
├─ SQLite or PostgreSQL
├─ Backups
└─ Replication

Storage
├─ File storage
├─ Model storage
└─ Cache storage
```

### Containerized Deployment

```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py"]
```

---

## Monitoring & Logging

### Logging Architecture

```
Application
    ↓
[Logger]
    ├─ INFO
    ├─ WARNING
    ├─ ERROR
    └─ DEBUG
    ↓
[Log Files]
├─ app.log
├─ error.log
└─ debug.log
```

### Metrics to Monitor

- Response times
- Error rates
- Database query performance
- Model inference time
- User activity
- Resource utilization

---

## Future Architecture Enhancements

1. **Microservices**
   - Separate service per agent
   - Independent deployment
   - Horizontal scaling

2. **API Layer**
   - REST API for external apps
   - GraphQL for flexible queries
   - WebSocket for real-time updates

3. **Advanced Caching**
   - Redis for distributed caching
   - Cache warming strategies
   - Invalidation patterns

4. **Message Queue**
   - Async job processing
   - Event streaming
   - Distributed processing

5. **ML Platform**
   - Model versioning
   - A/B testing framework
   - Model monitoring

---

**Last Updated**: 2026-06-11  
**Version**: 1.0.0

See [README.md](README.md) for overview or [AGENTS.md](AGENTS.md) for agent details.
