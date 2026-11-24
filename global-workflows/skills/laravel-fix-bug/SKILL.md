---
name: laravel-fix-bug
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Diagnose and fix a Laravel bug using a root-cause-driven approach while preserving architecture, security, tests, and documentation.
---

---

## 5. `fix_bug.md`

```md
# Fix Laravel Bug

## Goal

Diagnose and fix a Laravel bug using a root-cause-driven approach while preserving architecture, security, tests, and documentation.

## Mandatory Rules

- Do not patch blindly.
- Follow Plan → Implement → Review.
- Wait for approval before editing files.
- Prefer root-cause fixes over workarounds.
- Keep the change minimal.
- Add or update regression tests.
- Do not weaken validation, authorization, or architecture to make the bug disappear.

## Workflow

### 1. Plan

1. Understand the reported behavior and expected behavior.
2. Reproduce or inspect the failing flow.
3. Trace the request path:
    - Route
    - Middleware
    - Controller
    - Form Request
    - Policy
    - Service
    - Repository
    - Model
    - Resource
    - Response
4. Identify the likely root cause.
5. Check whether the bug is related to:
    - Validation
    - Authorization
    - Business logic
    - Query logic
    - N+1 or eager loading
    - Model casts
    - Relationships
    - Translation
    - Resource serialization
    - Exception handling
    - Queue / Job / Listener
    - Filament behavior
6. Propose the smallest safe fix.
7. Wait for approval.

### 2. Implement

After approval only:

1. Apply the minimal fix in the correct layer.
2. Keep Controllers thin.
3. Keep validation in Form Requests.
4. Keep queries in Repositories.
5. Keep business rules in Services.
6. Use custom domain exceptions when appropriate.
7. Return correct HTTP status codes.
8. Preserve unified API response format.
9. Add or update regression tests.
10. Update documentation if the API behavior changed.

### 3. Review

1. Run affected tests.
2. Run `php artisan test` when feasible.
3. Verify the bug is fixed.
4. Verify no unrelated behavior changed.
5. Summarize:
    - Root cause
    - Fix applied
    - Files changed
    - Tests added/updated
    - Documentation updated, if applicable
```
