---
name: flutter-security-check
description: >-
  Flutter Clean Architecture & S-S-W workflow: Perform a lightweight security and safety review of the selected feature, flow, or diff.
---

# Security Check

## Goal

Perform a lightweight security and safety review of the selected feature, flow, or diff.

## Mandatory Rules

- Do not change code unless explicitly asked.
- Focus on real project risks, not theoretical issues.
- Respect existing architecture.
- Never introduce unvalidated dependencies.
- Flag any request that introduces security risks or compromises maintainability.
- Always suggest safer alternatives.

## Workflow

### 1. Plan

1. Inspect the selected feature, flow, or diff.
2. Identify security-sensitive areas:
   - Authentication
   - Authorization
   - User input
   - API requests
   - File/media picking
   - External links
   - Permissions
   - Local storage
   - Destructive actions
   - Error handling
3. Identify the architecture layer where each risk appears.

### 2. Review Checklist

1. Verify user input uses project validators.
2. Verify forms use `validateAndScroll()`.
3. Verify API calls go through `ApiService`.
4. Verify endpoints are centralized in `ApiConstants`.
5. Verify errors do not fail silently.
6. Verify Blocs catch `ServerException` only.
7. Verify no raw secrets, tokens, or sensitive data are hardcoded.
8. Verify external actions use `LauncherManager`.
9. Verify permissions use `PermissionsManager`.
10. Verify destructive actions require confirmation dialogs.
11. Verify no raw navigation, dialogs, or snackbars are used.
12. Verify parsing uses `ParseUtils`.

### 3. Output Format

Return:

```md
## Security Check

### High Risk

- ...

### Medium Risk

- ...

### Low Risk

- ...

### Architecture Concerns

- ...

### Required Fixes

1. ...

### Safer Alternatives

- ...

### Final Recommendation

Proceed / Block / Proceed after fixes
```
