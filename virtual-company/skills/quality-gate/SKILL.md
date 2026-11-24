---
name: quality-gate
description: >-
  Verification and approval checklist enforced by Department Leads, QA,
  and the CEO before any deliverable is finalized and presented to the user.
---

# Company Quality Assurance Gate

Before any assignment is reported as complete, it must pass through this gate:

1. **Requirement Fulfillment:** Every item in the user's prompt must be explicitly addressed.
2. **Verification Evidence:**
   - For Code: Run tests, static analysis, or compiler verification. Provide exact command output.
   - For Copy/Docs: Verify spelling, grammar, tone consistency, and accuracy against actual systems.
   - For Architecture/Strategy: Verify feasibility, clear trade-offs, and risk identification.
3. **No Unintended Side-effects:** Verify that unrelated files or configs were not altered.
4. **Safety & Permission Check:** Ensure no private secrets, passwords, or destructive changes are included.
