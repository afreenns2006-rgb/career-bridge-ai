# 🎓 Career Bridge AI

> **AI-powered career guidance platform that helps students, fresh graduates, and job seekers move from confusion to a clear career plan.**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

## 🚀 Live Demo

| Resource | Link |
|---|---|
| 🌐 Live App | [Open Career Bridge AI](https://careerbridgeai-3kkasz5pd3ad7fzfry39e3.streamlit.app) |
| 💻 GitHub Repository | [github.com/afreenns2006-rgb/career-bridge-ai](https://github.com/afreenns2006-rgb/career-bridge-ai) |

---

## 📌 Problem Statement

Many students and fresh graduates struggle to make informed career decisions. They often do not know:

- whether their resume is job-ready,
- which career path matches their current skills,
- what skills they should learn next,
- where to find scholarships, schemes, internships, and opportunities,
- how to prepare for interviews and build relevant projects.

Career guidance is often scattered across different websites and platforms. This makes the process time-consuming, confusing, and inaccessible for many learners.

---

## 💡 Proposed Solution

**Career Bridge AI** brings career planning, resume feedback, opportunity discovery, learning guidance, and AI assistance into one beginner-friendly Streamlit app.

The platform helps users:

- analyze resumes,
- discover suitable careers,
- find scholarships and government schemes,
- explore internships and learning opportunities,
- generate personalized learning roadmaps,
- ask an AI Career Assistant for practical guidance,
- receive AI responses in English, Hindi, or Telugu.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📄 Resume Analyzer | Upload a PDF, DOCX, or TXT resume and get extracted skills, education, experience, ATS score, and improvement suggestions. |
| 💼 Career Mentor | Get career recommendations based on skills, education, and experience. |
| 🎓 Scholarship Finder | Discover scholarships using education level, income, GPA, and eligibility details. |
| 🏛️ Government Schemes | Find relevant government schemes with eligibility, benefits, required documents, and application steps. |
| 🚀 Opportunities Finder | Search internships, competitions, bootcamps, and career-building opportunities. |
| 🗺️ Learning Roadmap | Generate a structured learning plan with monthly goals, skills, and resources. |
| 🤖 AI Career Assistant | Ask career questions and receive roadmaps, resume tips, interview questions, skill suggestions, and project ideas. |
| 🌐 Multilingual Support | AI responses support English, Hindi, and Telugu. |
| 🔐 BYOK Support | Users can bring their own API key/token through a secure password input. |
| 🧠 Local AI with Ollama | Supports local inference through Ollama at `http://localhost:11434/api/generate`. |

---

## 🧠 AI Features

The **AI Career Assistant** can generate:

- career roadmap,
- resume improvement tips,
- interview questions,
- skill recommendations,
- project suggestions.

### Supported AI Modes

| Mode | Purpose |
|---|---|
| Local Ollama | Run AI locally using the default `llama3` model or any installed Ollama model. |
| BYOK | Use your own API key/token with an OpenAI-compatible endpoint. |
| Rule-based Fallback | Get simple offline guidance when no AI provider is configured. |

### Multilingual Responses

Use the sidebar language selector to choose:

- English
- Hindi
- Telugu

The AI Career Assistant responds in the selected language without breaking existing app features.

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Programming Language | Python |
| Web Framework | Streamlit |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Visualization | Plotly |
| AI Integration | Ollama API, BYOK-compatible API flow |
| Deployment | Streamlit Cloud |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```text
career-bridge-ai/
├── app.py                         # Main Streamlit application
├── config.py                      # Application settings and paths
├── database.py                    # SQLite database helper
├── resume_parser.py               # Resume parsing and ATS scoring
├── career_engine.py               # Career recommendation engine
├── scholarship_engine.py          # Scholarship matching engine
├── scheme_engine.py               # Government scheme recommendation engine
├── opportunity_engine.py          # Opportunity discovery engine
├── roadmap_engine.py              # Learning roadmap generator
├── services/
│   ├── ai_provider.py             # Ollama, BYOK, and fallback AI provider logic
│   └── language.py                # Language options and multilingual fallback content
├── data/
│   ├── careers.csv
│   ├── scholarships.csv
│   ├── schemes.csv
│   └── opportunities.csv
├── tests/                         # Pytest tests
├── requirements.txt               # Python dependencies
├── .env.example                   # Safe placeholder environment variables
├── README.md
└── LICENSE
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/afreenns2006-rgb/career-bridge-ai.git
cd career-bridge-ai
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
copy .env.example .env
```

On macOS/Linux:

```bash
cp .env.example .env
```

Keep real tokens only in `.env` or in the app UI. Do not commit real secrets.

### 5. Run the App

```bash
streamlit run app.py
```

Open the local app at:

```text
http://localhost:8501
```

---

## 🧠 Local AI Setup with Ollama

Career Bridge AI supports local AI inference using Ollama.

### Install and Start Ollama

```bash
ollama pull llama3
ollama serve
```

The app calls:

```text
http://localhost:11434/api/generate
```

In the app:

1. Open **AI Career Assistant**.
2. Select **Local Ollama**.
3. Use the default model `llama3` or enter another installed model.
4. Ask a career-related question.

If Ollama is not running, the app shows a friendly error message instead of crashing.

---

## 🔐 BYOK - Bring Your Own Key / Token

Career Bridge AI supports BYOK for users who want to connect their own AI provider.

- Select **BYOK** in the AI Career Assistant page.
- Enter your API key/token in the password field.
- Enter an OpenAI-compatible endpoint if needed.
- No API key is hardcoded in the project.
- `.env.example` contains placeholders only.

Default BYOK endpoint:

```text
https://api.openai.com/v1/chat/completions
```

---

## ☁️ Deployment Details

| Item | Details |
|---|---|
| Platform | Streamlit Cloud |
| Live Demo | [Career Bridge AI App](https://careerbridgeai-3kkasz5pd3ad7fzfry39e3.streamlit.app) |
| Repository | [GitHub Repo](https://github.com/afreenns2006-rgb/career-bridge-ai) |
| Main File | `app.py` |
| Dependency File | `requirements.txt` |

For Streamlit Cloud deployment:

1. Push the project to GitHub.
2. Connect the repository to Streamlit Cloud.
3. Set `app.py` as the entry point.
4. Add any private secrets in Streamlit Cloud secrets, not in Git.
5. Deploy the app.

---

## 🔍 How It Works

### Career Recommendation Algorithm

```text
Match Score = (Skill Match * 0.6) + (Experience Score * 0.4)
```

- Skill Match: matching skills divided by required skills.
- Experience Score: user experience compared with minimum role experience.
- Minimum recommendation threshold: 30%.

### Resume ATS Score

The resume analyzer checks:

- resume length,
- detected skills,
- education details,
- experience details,
- contact information,
- action keywords.

### Scholarship and Scheme Matching

The platform uses rule-based eligibility checks such as:

- education level,
- income,
- GPA,
- category,
- state,
- deadline and benefit information.

---

## 🧪 Testing

Run tests with:

```bash
pytest
```

Check Python syntax:

```bash
python -m py_compile *.py
```

---

## 🔒 Privacy and Security

- Resume files are processed locally by the app.
- Real API keys should never be committed.
- BYOK token input uses a password field.
- `.env.example` contains placeholder values only.
- Sensitive values should be stored in `.env` or deployment secrets.

---

## 🌱 Future Improvements

- More Indian regional languages.
- Real-time job market integration.
- Advanced resume scoring with AI feedback.
- Interview practice chatbot.
- Personalized dashboard for saved opportunities.
- Email or WhatsApp deadline reminders.
- Mentor matching for students.
- More scholarship and government scheme datasets.
- Better analytics and visual progress tracking.

---

<<<<<<< HEAD
## 👥 Team Members

| Name | Role |
|---|---|
| Afreen | Developer / Project Lead |
| Team Member 2 | Contributor |
| Team Member 3 | Contributor |

> Replace placeholder names with your final hackathon team details before submission.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit with a clear message.
5. Open a pull request.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgement

Career Bridge AI was built as a student-focused hackathon project to make career guidance more accessible, practical, and personalized.

**Status:** Hackathon Submission Ready ✅
=======


>>>>>>> 6637826e36fa71909091fdda4eef0a28cdd181f9
