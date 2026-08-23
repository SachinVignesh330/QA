# ParaBank Manual Testing Suite

This repository documents a manual QA testing effort for **ParaBank**, the demo online banking application ([parabank.parasoft.com](https://parabank.parasoft.com)). It covers requirements traceability, test case execution, and bug tracking across all core banking workflows.

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

### Notable open defects

- **BUG_003 / BUG_005 (Critical):** Transfer Funds accepts amounts exceeding balance and negative amounts, allowing negative balances and reversed fund flow.
- **BUG_007 (Critical):** Stored XSS payload in Bill Pay's Payee Name field triggers an unhandled application exception instead of being sanitized.
- **BUG_004 / BUG_006 (High):** Zero-amount transfers and over-balance Bill Pay payments are processed instead of rejected.
- **BUG_001 (Medium):** Duplicate personal details (same person, new username) are accepted on registration.
- **BUG_008 (Medium):** Logged-out account pages are still reachable via the browser back button and throw an error rather than redirecting.
- **BUG_002 (Low):** Phone number field accepts non-numeric input with no format validation.

## How to Use This Suite

1. **Start with the RTM** to see which requirements are covered and their pass/fail state at a glance.
2. **Drill into Test Cases** for the exact steps, test data, and expected vs. actual results behind any status.
3. **Check Bug Report** for full repro details on any `FAIL` result — each bug links back to its source requirement and test case.
4. Screenshot/evidence references (`SS_xxx`) in the Test Cases sheet correspond to supporting screenshots captured during execution (stored separately, not embedded in this workbook).

## Notes

- All test data uses fictitious/sample values (e.g. sample names, addresses) and is not real user data.
- Test execution date: 2026-08-21.
- This is a point-in-time manual regression pass; re-run affected test cases after each bug fix and update status/results accordingly.
