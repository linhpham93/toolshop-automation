# Toolshop Automation

## Purpose

Toolshop automation is a Python test suite built with **pytest** and **Playwright** for a demo online store. It tests sign-up, login, and product listing APIs alongside core UI flows like opening the homepage, sorting items, and viewing product details. It also includes hybrid UI-API tests covering login, searching and sorting products, viewing product details, and adding items to the cart.

## Project Structure

```text
├── .github/
│   └── workflows/
│       └── tests.yml       # GitHub Actions test workflow
├── pages/                  # Page object classes
├── tests/
│   ├── api/                # API test cases
│   ├── ui/                 # Browser UI test cases
│   ├── combined/           # Tests combining API and browser behavior
│   └── conftest.py         # Shared fixtures and pytest configuration hooks
├── pytest.ini              # pytest settings and custom markers
└── requirements.txt        # Python dependencies
```

## Setup

1. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment:**
   - **Windows:**
     ```bat
     .venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## How to Run

- **Run only tests marked with `api`:**
  ```bash
  pytest -m api
  ```

- **Run tests in parallel:**
  ```bash
  pytest -m api -n 2
  ```

- **Run tests with a custom `base_url`:**
  ```bash
  pytest --base-url https://your-target-url.example.com
  ```

## Reading the Report

Running pytest locally saves the self-contained HTML report to `report.html` relative to the test invocation directory. In GitHub Actions, [`tests.yml`](.github/workflows/tests.yml) uploads `report.html` as an artifact named `test-report` after every CI test step because the upload step uses `if: always()`.

## Known Limitations

- Currently, only API tests can run in CI/CD because the target website has bot protection that blocks direct UI interactions from GitHub Actions.