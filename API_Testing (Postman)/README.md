# Restful Booker API Testing & Quality Assurance Suite

##  Project Overview
This repository contains a comprehensive Quality Assurance (QA) test suite for the **Restful Booker API** (`https://restful-booker.herokuapp.com`). The objective of this project is to evaluate the functional correctness, validation mechanisms, security behavior, error handling, and edge-case resilience of the booking and authentication endpoints.

The suite encompasses end-to-end positive workflows, negative scenario testing, boundary value analysis (BVA), SQL injection security probing, and authentication enforcement checks.

---

## Project Scope

### In Scope
* **Authentication Module (`POST /auth`):**
  * Valid token generation using standard credentials.
  * Validation checks for invalid passwords, missing parameters, and empty request payloads.
* **Booking Module (`POST /booking`, `GET /booking`, `GET /booking/{id}`, `PUT /booking/{id}`, `DELETE /booking/{id}`):**
  * **Functional Testing:** Full CRUD operations for booking creation, retrieval, updates, and deletion.
  * **Negative & Edge-Case Testing:** Missing required fields, data type mismatches, negative price inputs, and illogical date ranges (e.g., check-out before check-in).
  * **Boundary Value Analysis (BVA):** Testing field length handling using long string inputs (200+ and 1,000 characters) on text fields.
  * **Query Parameter Filtering:** Testing retrieval filtering based on check-in and check-out date parameters.
* **Security & Authorization Testing:**
  * Testing authorization header enforcement (`Cookie` / `Basic Auth` tokens) on `PUT` and `DELETE` endpoints.
  * SQL Injection (SQLi) probing using raw input strings (e.g., `' OR 1=1 --`) across request bodies to test input sanitization.

### Out of Scope
* Performance, load, and stress testing (e.g., using JMeter or k6).
* Automated CI/CD pipeline integration (e.g., GitHub Actions / Jenkins runner configuration).
* UI or frontend integration testing.

---

## Test Execution Summary

| Metric | Count / Percentage |
| :--- | :--- |
| **Total Test Cases Executed** | **27** |
| **Passed** | **18** |
| **Failed** | **9** |
| **Pass Rate** | **66.67%** |

---

##  Test Suite Breakdown

The test suite consists of **27 structured test cases** covering the primary endpoints:

1. **Authentication (`POST /auth`):** Token generation and credential error handling.
2. **Booking Creation (`POST /booking`):** Standard payload acceptance, missing required fields, boundary testing, numerical data type validation, and input sanitization.
3. **Booking Retrieval (`GET /booking` & `GET /booking/{id}`):** ID lookups and date-range filtering.
4. **Booking Modification & Deletion (`PUT /booking/{id}` & `DELETE /booking/{id}`):** Payload updates, token verification, and non-existent resource handling.

---

##  Repository Structure

```text
.
├── docs/
│   ├── Restful_Booker_API_Suite.xlsx  # Complete Test Plan, Test Cases, & Bug Reports
│   ├── Test_Plan.pdf                   # QA Strategy & Scope Document
│   └── Defect_Report.pdf               # Detailed Bug Documentation
├── postman/
│   ├── Restful_Booker_Collection.json  # Exported Postman Collection (v2.1)
│   └── Restful_Booker_Environment.json # Postman Environment Config
├── .gitignore
└── README.md                           # Project Overview & Scope
```

---

##  Security & Data Integrity Analysis
* **SQL Injection Handling:** Tested using `' OR 1=1 --` payloads in text fields (`firstname`). The API safely escaped inputs and stored them as literal plain text without executing backend SQL code.
* **Authentication Enforcement:** Evaluated token parsing and header checks across state-modifying requests (`PUT`, `DELETE`).
