# Company Quality Standards & Verification Gates

## Engineering Standards
- **Zero Syntax & Linter Errors:** All code changes must pass language compilers and linters.
- **Architectural Harmony:** New code must align with existing codebase conventions and design patterns.
- **Separation of Concerns:** Business logic, data models, and presentation layers must remain decoupled.
- **Comprehensive Testing:** Critical paths require automated unit or widget/integration tests.

## Product & Design Standards
- **User-Centric Clarity:** Every feature must have clear user outcomes and edge-case definitions.
- **Accessibility Invariant:** UI components must satisfy WCAG 2.1 AA standards (contrast, touch targets >= 48dp, screen reader semantics).

## Security Invariants
- **No Hardcoded Secrets:** Credentials, private keys, and environment secrets must never appear in source code.
- **Defensive Input Validation:** All external input must be validated and sanitized.

## Review Sign-off Gate
Deliverables cannot be presented to the user as complete without verification evidence:
1. Static analysis output or compiler pass.
2. Automated test run or manual verification steps.
3. Clean git status / file delta summary.
