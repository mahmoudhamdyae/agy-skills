---
name: add-policy-authorization
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Add or update authorization using Laravel Policies or Gates while keeping authorization out of business logic.
---

# Add Policy Authorization

## Goal

Add or update authorization using Laravel Policies or Gates while keeping authorization out of business logic.

## Mandatory Rules

- Use Policies for resource-level authorization.
- Use Gates only for simple non-resource checks.
- Do not put authorization logic inside Services or Repositories.
- Controllers may trigger authorization using Laravel conventions.
- Tests must cover authorized and unauthorized users.
- Return correct status codes:
    - 401 for unauthenticated
    - 403 for unauthorized

## Workflow

### 1. Plan

1. Identify the protected resource or action.
2. Identify user roles and permissions.
3. Determine whether Policy or Gate is appropriate.
4. Identify affected endpoints, Filament actions, or Services.
5. Propose authorization plan and wait for approval.

### 2. Implement

After approval only:

1. Create or update the Policy.
2. Register the Policy if needed.
3. Add authorization checks in the correct presentation layer entry point.
4. Keep Services focused on business rules only.
5. Apply authorization to API endpoints and Filament actions where needed.
6. Add tests for:
    - Guest access
    - Authorized user
    - Unauthorized user
    - Edge roles

### 3. Review

1. Run authorization tests.
2. Verify 401 and 403 responses are correct.
3. Verify unified error response format.
4. Summarize:
    - Policy added/updated
    - Actions protected
    - Tests added
