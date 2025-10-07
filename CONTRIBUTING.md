# Contributing to PI-Engine

First off, thank you for considering contributing to PI-Engine! It's people like you that make PI-Engine such a great tool.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing Guidelines](#testing-guidelines)

---

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming and inclusive environment. Be respectful, constructive, and professional.

### Our Standards

✅ **Do:**
- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community

❌ **Don't:**
- Use sexualized language or imagery
- Make personal attacks or trolling
- Publish others' private information
- Engage in unprofessional conduct

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Exact steps to reproduce**
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, package versions)
- **Error messages and logs**
- **Screenshots** (if applicable)

**Bug Report Template:**
```markdown
## Bug Description
[Clear description]

## Steps to Reproduce
1. Step one
2. Step two
3. ...

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- OS: Windows 11
- Python: 3.13.7
- PI-Engine: 1.0.0

## Logs/Screenshots
[Paste relevant logs]
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Include:

- **Clear use case** - Why is this needed?
- **Proposed solution** - How would it work?
- **Alternatives considered** - What else did you think about?
- **Impact** - Who benefits and how?

### Pull Requests

We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`
2. If you've added code, add tests
3. Ensure the test suite passes
4. Update documentation
5. Issue the pull request

---

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Git
- Google Gemini API key

### Setup Steps

```powershell
# 1. Fork and clone the repository
git clone https://github.com/YOUR-USERNAME/Product_Intellegence_Engine.git
cd Product_Intellegence_Engine

# 2. Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your API key

# 5. Verify installation
python main.py --help
```

### Project Structure

```
Product_Intellegence_Engine/
├── config/              # Configuration files
├── scripts/             # Core modules
│   ├── scraper.py
│   ├── process_llm.py
│   └── visualize.py
├── utils/               # Utility functions
├── tests/               # Test files (add your tests here)
├── data/                # Data storage
└── main.py              # Entry point
```

---

## Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

```python
# Good ✅
def scrape_reviews(app_id: str, max_reviews: int = 1000) -> list:
    """
    Scrape reviews from Google Play Store.
    
    Args:
        app_id: Google Play Store app ID
        max_reviews: Maximum number of reviews to scrape
        
    Returns:
        List of review dictionaries
    """
    logger.info(f"Starting scrape for {app_id}")
    # Implementation
    return reviews

# Bad ❌
def scrapereviews(appid,maxreviews=1000):  # No type hints, unclear naming
    print("scraping")  # Use logger instead
    return r  # Unclear variable name
```

### Best Practices

**Do:**
- ✅ Use type hints for function parameters and returns
- ✅ Write docstrings for all functions and classes
- ✅ Use descriptive variable names (`review_count` not `rc`)
- ✅ Keep functions focused and small (<50 lines)
- ✅ Use logging instead of print statements
- ✅ Handle errors gracefully with try/except
- ✅ Add comments for complex logic
- ✅ Use config.py for constants, not magic numbers

**Don't:**
- ❌ Commit API keys or credentials
- ❌ Use wildcard imports (`from module import *`)
- ❌ Leave commented-out code
- ❌ Use global variables
- ❌ Ignore linter warnings

### Code Formatting

```powershell
# Install development tools
pip install black flake8 mypy

# Format code
black .

# Check style
flake8 .

# Type checking
mypy .
```

---

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**

```bash
# Good ✅
git commit -m "feat(scraper): add retry logic for failed requests"
git commit -m "fix(logger): handle Unicode characters on Windows"
git commit -m "docs(README): add installation troubleshooting section"

# Bad ❌
git commit -m "fixed stuff"
git commit -m "update"
git commit -m "asdfasdf"
```

### Atomic Commits

- One logical change per commit
- Commit messages explain **why**, not just **what**
- Each commit should pass tests

---

## Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Added tests for new features
- [ ] All tests pass locally
- [ ] Updated documentation
- [ ] Added/updated type hints
- [ ] Ran linters (black, flake8)
- [ ] Updated CHANGELOG.md

### PR Template

```markdown
## Description
[Brief description of changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Added unit tests
- [ ] Manual testing completed
- [ ] All tests pass

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed code
- [ ] Commented complex code
- [ ] Updated documentation
- [ ] No new warnings
- [ ] Added tests
- [ ] All tests pass
```

### Review Process

1. **Automated checks** - CI runs tests and linters
2. **Code review** - Maintainer reviews code
3. **Feedback** - Address review comments
4. **Approval** - Maintainer approves PR
5. **Merge** - Squash and merge to main

---

## Testing Guidelines

### Writing Tests

```python
# tests/test_scraper.py
import pytest
from scripts.scraper import validate_app_id

def test_validate_app_id_valid():
    """Test that valid app IDs are accepted."""
    assert validate_app_id("com.whatsapp") == True
    
def test_validate_app_id_invalid():
    """Test that invalid app IDs are rejected."""
    with pytest.raises(ValueError):
        validate_app_id("invalid_id")
        
def test_validate_app_id_empty():
    """Test that empty app IDs are rejected."""
    with pytest.raises(ValueError):
        validate_app_id("")
```

### Running Tests

```powershell
# Run all tests
pytest

# Run specific test file
pytest tests/test_scraper.py

# Run with coverage
pytest --cov=scripts --cov-report=html

# Run with verbose output
pytest -v
```

### Test Coverage

- Aim for **80%+ code coverage**
- Test edge cases and error conditions
- Test with sample data before live API calls

---

## Development Workflow

### Feature Development

```bash
# 1. Create feature branch
git checkout -b feat/add-ios-support

# 2. Make changes and commit
git add .
git commit -m "feat(scraper): add iOS App Store scraper"

# 3. Push to your fork
git push origin feat/add-ios-support

# 4. Open Pull Request on GitHub
```

### Bug Fixes

```bash
# 1. Create bugfix branch
git checkout -b fix/unicode-error

# 2. Fix and test
git add .
git commit -m "fix(logger): handle emoji characters on Windows"

# 3. Push and PR
git push origin fix/unicode-error
```

---

## Getting Help

### Resources

- **Documentation**: [README.md](README.md)
- **Issues**: [GitHub Issues](https://github.com/raindragon14/Product_Intellegence_Engine/issues)
- **Discussions**: [GitHub Discussions](https://github.com/raindragon14/Product_Intellegence_Engine/discussions)

### Questions?

- Check existing issues and discussions first
- Ask in [GitHub Discussions](https://github.com/raindragon14/Product_Intellegence_Engine/discussions)
- Tag maintainers if urgent: @raindragon14

---

## Recognition

Contributors will be:
- Added to CHANGELOG.md for their contributions
- Mentioned in release notes
- Listed in README.md contributors section

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to PI-Engine! 🚀**
