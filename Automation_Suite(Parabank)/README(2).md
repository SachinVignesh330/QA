# 🎭 ParaBank E2E Test Automation Framework

A professional End-to-End (E2E) web automation framework built with **Python**, **Playwright**, and **Pytest**. This suite tests the core authentication and user flows of the [ParaBank](https://parabank.parasoft.com) application using modern QA architecture patterns, dynamic data generation, and comprehensive reporting.

---

## 🚀 Key Features

* **Page Object Model (POM):** Scalable, maintainable object-oriented structure separating page locators/actions from test logic.
* **Dynamic Data Generation:** Uses dynamic user generation to ensure isolated, repeatable test execution without data collisions.
* **Smart Failure Handling (`@pytest.mark.xfail`):** Built-in tracking for live backend application bugs (e.g., ParaBank 500 internal server errors on invalid login).
* **Multi-Browser Testing:** Configured for cross-browser execution across Firefox and Chromium.
* **Self-Contained HTML Reports:** Generates standalone execution reports with embedded CSS and failure logs for easy sharing.

---

## 🛠 Tech Stack

* **Language:** Python 3.10+
* **Automation Tool:** Playwright Python
* **Test Runner:** Pytest
* **Reporting:** Pytest-HTML
* **Design Pattern:** Page Object Model (POM)

---

## 📁 Project Structure

```text
QA-Automation-ParaBank/
├── Config/
│   └── detail_gen.py        # Dynamic user data generator (timestamped credentials)
├── Pages/
│   ├── base_page.py         # Shared web driver actions & element wrappers
│   ├── login.py             # Login Page Object (locators & actions)
│   └── registration.py      # Registration Page Object (locators & actions)
├── Tests/
│   └── login_test.py        # E2E Pytest login test suite (TC_011 to TC_016)
├── report.html              # Generated self-contained execution report
├── requirements.txt         # Project dependencies
└── README.md                # Framework documentation
```

---

## ⚡ Quick Start & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/QA-Automation-ParaBank.git
cd QA-Automation-ParaBank
```

### 2. Create and Activate Virtual Environment
```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies & Playwright Browsers
```bash
pip install -r requirements.txt
playwright install
```

---

## 🧪 Executing Tests

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

## 📊 Test Coverage Summary

| Test ID | Scenario Description | Expected Outcome | Execution Result | Notes / Bug Reference |
| :--- | :--- | :--- | :--- | :--- |
| **TC_011** | Valid User Login | Successful redirection to account overview | **PASSED** | Dynamic user registration via fixture |
| **TC_012** | Invalid Password Login | User-friendly error message displayed | **XFAIL** | Application throws 500 Internal Error (`BUG_008`) |
| **TC_013** | Non-Existent User Login | User-friendly error message displayed | **XFAIL** | Application throws 500 Internal Error (`BUG_009`) |
| **TC_014** | Empty Fields Login | "Please enter a username and password." | **PASSED** | Client-side validation confirmed |
| **TC_016** | Leading Spaces in Username | Graceful handling or verification error | **XFAIL** | Application throws 500 Internal Error (`BUG_010`) |

---

## 🐛 Defect Tracking & Known Issues

The target application (ParaBank) has known server-side defects when handling invalid credentials. Rather than removing these valid test scenarios, they are annotated with Pytest’s `@pytest.mark.xfail`:

```python
@pytest.mark.xfail(reason="Known Bug: Server returns 500 error instead of validation text")
def test_TC_012(page, registered_user):
    # Test logic
```
This ensures test suite integrity while alerting developers to unhandled backend Java exceptions.

---

## 📬 Contact & Portfolio

Developed as part of a **Software Quality Assurance / Automation Portfolio**.  
* **Author:** Sachin
* **Role:** Quality Assurance Engineer Intern / Trainee
