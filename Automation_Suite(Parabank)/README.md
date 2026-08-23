#  ParaBank Test Automation Framework

A  web automation framework built with **Python**, **Playwright**, and **Pytest**. This suite tests the core authentication and user flows of the [ParaBank](https://parabank.parasoft.com) application using modern QA architecture patterns, dynamic data generation, and comprehensive reporting.

---

## Key Features

* **Page Object Model (POM):** Scalable, maintainable object-oriented structure separating page locators/actions from test logic.
* **Dynamic Data Generation:** Uses dynamic user generation to ensure isolated, repeatable test execution without data collisions.
* **Multi-Browser Testing:** Configured for cross-browser execution across Firefox and Chromium.
* **Self-Contained HTML Reports:** Generates standalone execution reports with embedded CSS and failure logs for easy sharing.

---

##  Tech Stack

* **Language:** Python 3.10+
* **Automation Tool:** Playwright Python
* **Test Runner:** Pytest
* **Reporting:** Pytest-HTML
* **Design Pattern:** Page Object Model (POM)

---

## Project Structure

Automation_Suite(ParaBank)/
├── Config/
│   └── detail_gen.py                # Dynamic user data & credentials generator
├── Pages/
│   ├── billpay.py                   # Bill Payment Page Object
│   ├── login.py                     # Login Page Object
│   ├── registration.py              # User Registration Page Object
│   └── request_loan.py              # Request Loan Page Object
├── Reports/
│   ├── billpay_test_report.html     # Execution report for Bill Pay test suite
│   ├── registration_report.html     # Execution report for Registration test suite
│   └── requestloan_test_report.html # Execution report for Request Loan test suite
├── Tests/
│   ├── billpay_test.py              # E2E Bill Payment tests
│   ├── login_test.py                # E2E Login & Authentication tests
│   ├── registration_test.py         # E2E Registration flow tests
│   └── requestloan_test.py          # E2E Loan Application tests
├── README.md                        # Framework documentation
└── requirements.txt                 # Project dependencies

---


## Executing Tests

### Run Login Test Suite (Headed Firefox)
```bash
python -m pytest Tests/login_test.py --headed --browser firefox
```

### Run Tests Headlessly with HTML Report
```bash
python -m pytest Tests/login_test.py --browser firefox --html=report.html --self-contained-html
```

### Capture Screenshots Automatically on Failure
```bash
python -m pytest Tests/login_test.py --browser firefox --screenshot=only-on-failure --html=report.html --self-contained-html
```

---

## Test Coverage Summary

* **4 main modules covered - Registration, Login, Bill pay, Request Loan
* **19 Test cases have been automated.

##  Defect Tracking & Known Issues

The target application (ParaBank) has known server-side defects when handling invalid credentials. Rather than removing these valid test scenarios, they are annotated with Pytest’s `@pytest.mark.xfail`:


 
* **Author:** Sachin
* **Role:** Quality Assurance Engineer Intern / Trainee
