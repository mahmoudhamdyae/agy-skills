---
name: laravel-security-check
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Perform a security review of a Laravel endpoint, module, diff, service, repository, or Filament resource.
---

# Laravel Security Check

## Goal

Perform a security review of a Laravel endpoint, module, diff, service, repository, or Filament resource.

## Mandatory Rules

- Do not modify files unless explicitly asked.
- Focus on real risks.
- Never suggest shortcuts that bypass authorization, validation, or safe query practices.
- All proposed fixes must preserve Clean Architecture and Laravel conventions.

## Workflow

### 1. Inspect

1. Review the selected code or diff.
2. Identify sensitive areas:
    - Authentication
    - Authorization
    - Validation
    - Mass assignment
    - Password handling
    - Sensitive logs
    - Raw SQL
    - Public endpoints
    - File uploads
    - External API calls
    - Queues
    - Filament actions
    - Destructive actions

### 2. Checklist

1. Verify authorization uses Policies or Gates.
2. Verify resource-level permissions are not inside business logic.
3. Verify Form Requests are used for validation.
4. Verify no `$request->validate()` inside Controllers.
5. Verify no `Validator::make()` inside Controllers or Services.
6. Verify passwords use `Hash::make()`.
7. Verify sensitive data is not logged or returned.
8. Verify `$fillable` is explicit.
9. Verify `$guarded = []` is not used.
10. Verify raw SQL uses bindings.
11. Verify public endpoints use throttle middleware.
12. Verify exceptions do not expose stack traces.
13. Verify destructive Filament actions require confirmation.
14. Verify file uploads validate type, size, and visibility.
15. Verify external API calls are queued when long-running.

### 3. Output Format

```md
## Security Review

### High Risk

- ...

### Medium Risk

- ...

### Low Risk

- ...

### Required Fixes

1. ...

### Recommended Improvements

- ...

### Final Decision

Proceed / Block / Proceed after fixes
```
