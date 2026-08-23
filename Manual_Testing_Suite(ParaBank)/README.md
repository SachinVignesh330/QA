# ParaBank Manual Testing Suite

This is a manual QA testing for **ParaBank**, the demo online banking application ([parabank.parasoft.com](https://parabank.parasoft.com)). It covers requirements traceability, test case execution, and bug tracking across all core banking workflows.

## Contents

The suite lives in `Parabank_Suite.xlsx` and is organized into three linked sheets:

| Sheet | Purpose |
|---|---|
| **RTM** | Requirements Traceability Matrix — maps each requirement to its test case(s), test status, and any linked bug |
| **Test Cases** | Full manual test case log — steps, test data, expected vs. actual results, status, and evidence reference |
| **Bug Report** | Defect log for every failed test — repro steps, expected vs. actual behavior, severity, and priority |

Each sheet is cross-referenced by ID (`REQ-xxx` → `TC_xxx` → `BUG_xxx`), so any requirement can be traced end-to-end from spec to test to defect.

## Modules Covered

- Registration
- Login
- Accounts Overview
- Transfer Funds
- Bill Pay
- Find Transactions
- Update Contact Info
- Request Loan
- Log Out

Test types include **Positive**, **Negative**, **Edge**, and **Security** cases (e.g. SQL injection, stored XSS, session/auth bypass via URL and browser back-button).

## Current Results Summary

| Metric | Count |
|---|---|
| Requirements tracked | 33 |
| Requirements passing | 26 |
| Requirements failing | 7 |
| Test cases executed | 37 |
| Test cases passed | 29 |
| Test cases failed | 8 |
| Open bugs | 8 |

**Bugs by severity:** 3 Critical · 2 High · 2 Medium · 1 Low — all currently **Open**.




- This is a point-in-time manual regression pass; re-run affected test cases after each bug fix and update status/results accordingly.
