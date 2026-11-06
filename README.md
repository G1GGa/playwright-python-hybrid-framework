# Hybrid QA Automation Framework (Python, Playwright & Requests)

[![Python](https://img.shields.io/badge/Python-3.15%2B-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-UI%20Testing-green.svg)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/Pytest-Test%20Runner-orange.svg)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust, enterprise-grade hybrid test automation framework built from scratch using **Python**. This repository demonstrates advanced Software Development Engineer in Test (SDET) practices, combining **UI Test Automation** via Playwright with **API Testing** using Requests, structured around the **Page Object Model (POM)** architectural pattern.

---

## 🚀 Key Features

* **Hybrid Architecture**: Unified test suite covering both API endpoints and modern Web UIs.
* **Page Object Model (POM)**: Complete separation of test logic from page locators and actions, ensuring high maintainability and DRY principles.
* **Global Test Lifecycle & Logging**: Centralized configuration via `conftest.py` with custom logging to track test execution streams.
* **Robust Assertion Handling**: Validating HTTP status codes, JSON payloads, and dynamic UI states.
* **Scalable Test Runner**: Powered by `pytest` with parallel execution readiness and detailed terminal reporting (`-v`).

---

## 🛠️ Tech Stack

* **Programming Language**: Python
* **UI Automation**: Playwright (Async/Sync API)
* **API Testing**: Requests library
* **Test Runner**: Pytest
* **Design Pattern**: Page Object Model (POM)

---

## 📂 Project Structure

```text
playwright_python_framework/
│
├── pages/                  # Page Object Model classes (UI elements & actions)
│   └── login_page.py       # Login functionality abstraction
│
├── tests/                  # Test suites
│   ├── test_api.py         # REST API test cases (ReqRes endpoints)
│   └── test_ui.py          # UI browser test cases (SauceDemo)
│
├── logs/                   # Execution logs and reporting outputs
├── conftest.py             # Global fixtures, hooks, and logging setup
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation