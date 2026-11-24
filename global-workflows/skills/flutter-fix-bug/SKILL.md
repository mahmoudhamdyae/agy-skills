---
name: flutter-fix-bug
description: >-
  Flutter Clean Architecture & S-S-W workflow: Diagnose and fix a bug using a minimal, root-cause-driven approach without breaking architecture, tests, or existing behavior.
---

---

## 3. `fix_bug.md`

```md
# Fix Bug

## Goal

Diagnose and fix a bug using a minimal, root-cause-driven approach without breaking architecture, tests, or existing behavior.

## Mandatory Rules

- Do not patch blindly.
- Follow Plan → Implement → Review.
- Wait for approval before changing files.
- Prefer root-cause fixes over workaround fixes.
- Modify only the necessary files.
- Add or update regression tests.
- Preserve Clean Architecture and existing project patterns.
- Never introduce architecture shortcuts to fix a bug quickly.

## Workflow

### 1. Plan

1. Understand the reported bug and expected behavior.
2. Inspect the relevant feature, starting from the UI entry point if applicable.
3. Trace the flow:
   UI → Section → Bloc/Cubit → UseCase → Repository → DataSource → ApiService.
4. Identify the smallest likely root cause.
5. Check whether the issue belongs to:
   - UI rendering
   - Section interaction
   - Bloc/Cubit state transition
   - UseCase logic
   - Repository mapping
   - DataSource/API behavior
   - DTO parsing
   - Mapper conversion
   - Pagination
   - Validation
   - Localization
6. Propose a fix plan with trade-offs.
7. Wait for approval.

### 2. Implement

After approval only:

1. Apply the smallest safe code change.
2. Respect the correct architecture layer.
3. Use Core Foundation utilities before writing custom logic.
4. If parsing is involved, use `ParseUtils`.
5. If navigation is involved, use `context.push`, `context.go`, or `context.pop`.
6. If user feedback is involved, use the relevant manager:
   - `DialogsManager`
   - `SnackBarsManager`
   - `BottomSheetsManager`
7. If form submission is involved:
   - Use `validateAndScroll()`.
   - Call `HelperFunctions.unFocusKeyboard()`.
8. Add or update regression tests for the bug.

### 3. Review

1. Run affected tests.
2. Verify the bug is fixed.
3. Verify no unrelated behavior changed.
4. Verify architecture boundaries are still respected.
5. Summarize:
   - Root cause
   - Files changed
   - Tests added/updated
   - Verification result
```
