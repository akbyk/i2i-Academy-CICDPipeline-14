# i2i Academy CI/CD Pipeline - Assignment 14

A practical internship assignment demonstrating the implementation of a CI/CD pipeline using GitHub Actions, featuring automated testing and deployment workflows.

## 📋 Overview

This project implements a complete CI/CD pipeline that automates testing and deployment processes. It includes:
- **Unit testing** with pytest
- **UI testing** with Selenium
- **Automated deployment** on successful test completion

## 🛠️ Technologies Used

- **Python 3.11**
- **pytest** - Unit testing framework
- **Selenium** - Browser automation for UI testing
- **GitHub Actions** - CI/CD orchestration

## 📁 Project Structure

```
├── app.py                          # Main application with email validation
├── test_app.py                     # Unit tests for app.py
├── test_ui.py                      # UI tests using Selenium
├── requirements.txt                # Python dependencies
└── .github/workflows/              # GitHub Actions workflows
    └── i2i-Academy-CICDPipeline-14.yml
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/akbyk/i2i-Academy-CICDPipeline-14.git
   cd i2i-Academy-CICDPipeline-14
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests Locally

Run unit tests:
```bash
pytest test_app.py -v
```

Run UI tests:
```bash
pytest test_ui.py -v
```

Run all tests:
```bash
pytest -v
```

## 📝 Features

### Email Validation (app.py)
The main application includes an `is_valid_email()` function that validates email addresses using regex:
- Accepts standard email formats
- Validates domain structure with TLD
- Supports subdomains and special characters

### Unit Tests (test_app.py)
Comprehensive tests for email validation covering:
- ✅ Valid email formats
- ❌ Invalid email formats
- Edge cases (empty strings, missing domains)

### UI Tests (test_ui.py)
Selenium-based tests for UI functionality:
- Headless browser automation
- Page title verification
- Cross-browser compatibility

## 🔄 CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **Checks out code** from the repository
2. **Sets up Python 3.11** environment
3. **Installs dependencies** from requirements.txt
4. **Runs unit tests** with pytest
5. **Runs UI tests** with Selenium (headless mode)
6. **Confirms deployment** when all tests pass

The pipeline triggers on **all branch pushes**, ensuring continuous validation.

## 📦 Dependencies

- `pytest==8.3.3` - Testing framework
- `selenium==4.25.0` - Browser automation library

## ✨ Learning Outcomes

This assignment demonstrates:
- Writing unit tests and UI tests
- Configuring GitHub Actions workflows
- Implementing automated testing in CI/CD pipelines
- Best practices for test organization
- Headless browser testing for UI validation

## 📧 Author

Created as part of the i2i Academy internship program.

---

**Note:** The UI test currently points to `https://www.example.com`. Update the URL to test against your actual application.
