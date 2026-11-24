---
name: flutter-cleanup
description: >-
  Flutter Clean Architecture & S-S-W workflow: Clean low-risk code quality issues while preserving behavior and architecture.
---

---

## 10. `cleanup.md`

```md
# Cleanup

## Goal

Clean low-risk code quality issues while preserving behavior and architecture.

## Mandatory Rules

- Follow Plan → Implement → Review.
- Wait for approval before changing files.
- Do not change behavior.
- Do not introduce new dependencies.
- Do not restructure large areas without approval.
- Keep the footprint minimal.
- Use Core Foundation First.

## Workflow

### 1. Plan

1. Inspect the selected files or current diff.
2. Identify low-risk cleanup opportunities:
   - Unused imports
   - Dead code
   - Duplicate small logic
   - Non-descriptive names
   - Missing `const`
   - Raw spacing widgets
   - Raw colors
   - Raw text widgets
   - Raw navigation
   - Raw print statements
   - Hardcoded strings
   - Heavy logic inside `build`
3. Separate safe cleanup from risky refactoring.
4. Propose the cleanup plan and wait for approval.

### 2. Implement

After approval only:

1. Remove unused imports and dead code.
2. Add `const` where possible.
3. Replace raw `print` with `Log`.
4. Replace raw navigation with context navigation extensions.
5. Replace hardcoded strings with `StringsManager`.
6. Replace raw spacing with `.ph` and `.pw`.
7. Replace raw sizes with `.wi()`, `.he()`, `.rad()`, `.sp()`.
8. Replace raw colors with context theme extensions.
9. Replace raw project-equivalent widgets with core widgets.
10. Extract non-trivial callbacks from `build`.
11. Keep each class/widget/entity in its own file.

### 3. Review

1. Run format, analyze, and affected tests where available.
2. Verify behavior did not change.
3. Verify no architecture rules were violated.
4. Summarize:
   - Cleanup performed
   - Files changed
   - Tests/checks run
   - Remaining cleanup opportunities
```
