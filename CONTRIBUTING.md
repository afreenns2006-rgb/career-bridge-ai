# Contributing to Career Bridge AI

Thank you for your interest in contributing to Career Bridge AI! This document provides guidelines and instructions for contributing to our project.

Quality gates, security scanning, pre-commit setup, and coverage commands are documented in [docs/QUALITY.md](docs/QUALITY.md).

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Submitting Changes](#submitting-changes)
- [Review Process](#review-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Questions?](#questions)

---

## Code of Conduct

Please read and adhere to our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). We are committed to providing a welcoming and inclusive community.

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- GitHub account
- Familiarity with Python and Git workflows

### Fork and Clone

1. **Fork the Repository**
   - Click "Fork" on the GitHub repository page
   - This creates your own copy of the project

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/career-bridge-ai.git
   cd career-bridge-ai
   ```

3. **Add Upstream Remote**
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/career-bridge-ai.git
   ```

---

## Development Setup

### Step 1: Create a Virtual Environment

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development tools
```

### Step 3: Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### Step 4: Set Environment Variables

```bash
cp .env.example .env
# Edit .env with your configuration
```

### Step 5: Initialize Database

```bash
python scripts/init_db.py
```

### Step 6: Verify Setup

```bash
pytest tests/ -v
```

---

## Making Changes

### Create a Branch

1. **Update your local repository**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

   **Branch naming conventions:**
   - Features: `feature/feature-name`
   - Bug fixes: `bugfix/bug-description`
   - Documentation: `docs/documentation-name`
   - Experiments: `experiment/experiment-name`

### Make Your Changes

- Write clear, concise code
- Follow the coding standards (see below)
- Add tests for new functionality
- Update documentation as needed

---

## Coding Standards

### Python Style Guide

We follow PEP 8 with some enhancements:

1. **Formatting**
   ```python
   # Good: Clear and concise
   def extract_skills(resume_text, threshold=0.7):
       """
       Extract skills from resume text.
       
       Args:
           resume_text (str): Text content of resume
           threshold (float): Confidence threshold
           
       Returns:
           list: Extracted skills
       """
       skills = []
       # Implementation
       return skills
   ```

2. **Naming Conventions**
   - Variables: `snake_case`
   - Classes: `PascalCase`
   - Constants: `UPPER_CASE`
   - Functions: `snake_case`
   - Private methods: `_private_method()`

3. **Imports**
   ```python
   # Standard library imports
   import os
   import sys
   from pathlib import Path
   
   # Third-party imports
   import pandas as pd
   import numpy as np
   from sklearn.model_selection import train_test_split
   
   # Local imports
   from src.database import Database
   from src.utils import sanitize_input
   ```

4. **Type Hints**
   ```python
   def calculate_ats_score(resume_text: str) -> float:
       """Calculate ATS score for resume."""
       score: float = 0.0
       # Implementation
       return score
   ```

5. **Docstrings**
   ```python
   def analyze_resume(file_path: str, output_format: str = "json") -> dict:
       """
       Analyze a resume file and extract information.
       
       This function reads a resume file (PDF/DOCX/TXT), extracts
       text content, analyzes it using NLP models, and returns
       structured information about skills, experience, and education.
       
       Args:
           file_path (str): Path to the resume file.
           output_format (str): Format of output ('json' or 'dict').
               Defaults to 'json'.
       
       Returns:
           dict: Dictionary containing:
               - 'skills' (list): Extracted skills
               - 'experience' (list): Work experience
               - 'education' (list): Education details
               - 'ats_score' (float): ATS compatibility score
       
       Raises:
           FileNotFoundError: If file doesn't exist.
           ValueError: If file format is not supported.
       
       Example:
           >>> result = analyze_resume('resume.pdf')
           >>> print(result['skills'])
           ['Python', 'Machine Learning']
       """
   ```

### File Organization

```
src/
├── __init__.py
├── resume_analyzer.py      # Resume analysis logic
├── career_recommender.py   # Career recommendation engine
├── scholarship_matcher.py  # Scholarship matching
├── scheme_matcher.py       # Government scheme matching
├── opportunity_discoverer.py  # Opportunity discovery
├── roadmap_generator.py    # Learning roadmap generation
├── database.py             # Database operations
├── utils.py                # Utility functions
└── config.py               # Configuration
```

---

## Testing Guidelines

### Writing Tests

```python
import pytest
from src.resume_analyzer import ResumeAnalyzer

class TestResumeAnalyzer:
    """Test suite for ResumeAnalyzer."""
    
    @pytest.fixture
    def analyzer(self):
        """Create analyzer instance."""
        return ResumeAnalyzer()
    
    def test_extract_skills_from_resume(self, analyzer):
        """Test skill extraction from resume."""
        text = "Experienced Python developer with ML expertise"
        skills = analyzer.extract_skills(text)
        assert "Python" in skills
        assert "Machine Learning" in skills
    
    def test_invalid_file_handling(self, analyzer):
        """Test handling of invalid files."""
        with pytest.raises(FileNotFoundError):
            analyzer.analyze_resume("nonexistent.pdf")
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_resume_analyzer.py

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run with verbose output
pytest tests/ -v

# Run with markers
pytest tests/ -m "not slow"
```

### Test Coverage Requirements

- New code should include focused tests. The repository-wide CI threshold starts at 1% while baseline coverage is established.
- All public functions should have tests
- Edge cases should be covered

---

## Submitting Changes

### Commit Guidelines

```bash
# Make meaningful commits
git add src/resume_analyzer.py tests/test_resume_analyzer.py

git commit -m "Improve skill extraction accuracy

- Enhanced NLP pipeline for better skill recognition
- Added support for skill variations and synonyms
- Increased accuracy from 78% to 85%

Fixes #123"
```

**Commit message format:**
```
<Type>: <Subject>

<Body - explain what and why, not how>

<Footer - reference issues and breaking changes>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Test additions/modifications

### Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### Create Pull Request

1. Go to the original repository on GitHub
2. Click "New Pull Request"
3. Select your branch
4. Provide a clear title and description
5. Link related issues
6. Submit the PR

---

## Pull Request Guidelines

### PR Title Format
```
[Component] Brief description of changes

Examples:
- [Resume Analyzer] Improve skill extraction accuracy
- [Career Recommender] Add salary prediction feature
- [Tests] Increase test coverage for database module
```

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
- [ ] Added unit tests
- [ ] Updated existing tests
- [ ] All tests pass locally

## Checklist
- [ ] My code follows the style guidelines
- [ ] I've updated relevant documentation
- [ ] I've added necessary tests
- [ ] All tests pass

## Related Issues
Fixes #123
```

---

## Review Process

### Code Review

1. **At least 2 approvals required** before merging
2. **All checks must pass**:
   - GitHub Actions (CI/CD)
   - Code coverage reporting
   - Linting (flake8, pylint)
   - Tests (pytest)

3. **Review comments**:
   - Be respectful and constructive
   - Focus on code, not person
   - Suggest improvements
   - Ask questions if unclear

4. **Addressing feedback**:
   - Respond to all comments
   - Update your branch with changes
   - Re-request review when ready

### Merge

- Use "Squash and merge" for small PRs
- Use "Create a merge commit" for larger features
- Delete branch after merging

---

## Reporting Bugs

### Bug Report Template

**Title**: `[Bug] Brief description`

**Description**:
```markdown
## Description
Brief description of the bug.

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen.

## Actual Behavior
What actually happens.

## Environment
- OS: Windows/macOS/Linux
- Python Version: 3.9/3.10/3.11
- Branch: main/development

## Screenshots/Logs
If applicable, add screenshots or error logs.

## Severity
- [ ] Critical
- [ ] High
- [ ] Medium
- [ ] Low
```

---

## Suggesting Features

### Feature Request Template

**Title**: `[Feature] Brief description`

**Description**:
```markdown
## Problem Statement
What problem does this solve?

## Proposed Solution
How should this be implemented?

## Benefits
Why is this important?

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Additional Context
Any other relevant information.
```

---

## Documentation

### Adding Documentation

1. **Code Comments**
   - Comment complex logic
   - Explain "why", not "what"
   - Keep comments updated

2. **Docstrings**
   - Use Google-style docstrings
   - Include examples
   - Document parameters and return values

3. **README Updates**
   - Update if adding features
   - Document new commands/usage
   - Add to table of contents

4. **Architecture Docs**
   - Update if changing architecture
   - Document new components
   - Include diagrams if helpful

---

## Development Tools

### Recommended Tools

- **IDE**: VS Code, PyCharm, Sublime Text
- **Linting**: pylint, flake8
- **Formatting**: black, autopep8
- **Testing**: pytest, pytest-cov
- **Git GUI**: GitHub Desktop, SourceTree

### Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit

# Setup hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

---

## Troubleshooting

### Common Issues

**Issue**: Tests failing locally but passing in CI
```bash
# Ensure dependencies are updated
pip install -r requirements.txt --upgrade

# Clear pytest cache
pytest --cache-clear
```

**Issue**: Import errors
```bash
# Reinstall package in development mode
pip install -e .
```

**Issue**: Database errors
```bash
# Reset database
rm data/career_bridge.db
python scripts/init_db.py
```

---

## Questions?

- **Documentation**: Check [docs/](docs/) directory
- **Issues**: Browse [GitHub Issues](https://github.com/yourname/career-bridge-ai/issues)
- **Discussions**: Join [GitHub Discussions](https://github.com/yourname/career-bridge-ai/discussions)
- **Email**: contribute@careerbridgeai.com

---

## Recognition

Contributors are recognized in:
- `CONTRIBUTORS.md` file
- GitHub profile
- Release notes
- Project website

---

Thank you for contributing to Career Bridge AI! 🚀

**Last Updated**: 2026-06-11  
**Version**: 1.0.0
