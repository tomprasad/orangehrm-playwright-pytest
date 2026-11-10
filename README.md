# OrangeHRM Demo Hybrid Automation Framework

A portfolio-ready UI + API hybrid test automation framework for the OrangeHRM open-source demo application.

**Stack:** Python · Playwright · Pytest · GitHub Actions · Allure / pytest-html

**Demo Application:** https://opensource-demo.orangehrmlive.com/

## Key Features (Planned / In Progress)

- Page Object Model (POM) architecture
- Reusable fixtures (including role-based authentication for Admin & Employee)
- Data-driven and hybrid (API + UI) tests
- Cross-browser execution (Chromium, Firefox, WebKit)
- CI/CD pipeline with GitHub Actions (browser matrix)
- Reporting with screenshots, traces, and HTML/Allure reports
- Clean configuration management (`.env` + settings)

## Project Status

Currently in **Phase 1: Setup & Planning**.  
See the project tracker for full task list and progress.

## Quick Start

*(Will be updated as the framework is built)*

```bash
# Clone the repo
git clone https://github.com/tomprasad/orangehrm-playwright-pytest
cd orangehrm-playwright-pytest

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies (requirements.txt coming soon)
pip install -r requirements.txt

# Install Playwright browsers
playwright install

Project Structure (Target)Text├── pages/          # Page Object classes
├── tests/          # Test modules
├── config/         # Settings and configuration
├── data/           # Test data files
├── utils/          # Helpers and utilities
├── conftest.py     # Pytest fixtures
├── pytest.ini
└── requirements.txt

Running Tests(Commands will be added once the framework is ready)

License
MIT
