---
name: laravel-generate-tests
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Generate or update Pest tests for API endpoints, Services, Repositories, Form Requests, Policies, Jobs, Events, and Filament behavior where applicable.
---

# Generate Laravel Tests

## Goal

Generate or update Pest tests for API endpoints, Services, Repositories, Form Requests, Policies, Jobs, Events, and Filament behavior where applicable.

## Mandatory Rules

- Testing is not optional.
- Follow Plan → Implement → Review.
- Wait for approval before writing files.
- Use Pest.
- Use `RefreshDatabase` in Feature tests.
- Use Factories for test data.
- Never hardcode database IDs.
- Mock external APIs and third-party services.
- Test behavior, not implementation details.
- Run `php artisan test` before marking the task as complete.

## Workflow

### 1. Plan

1. Inspect the selected endpoint, class, module, or feature.
2. Identify what must be tested:
    - API endpoint
    - Service logic
    - Repository query behavior
    - Form Request validation
    - Policy / Gate authorization
    - Job / Listener behavior
    - Filament resource behavior
3. Identify existing test conventions.
4. List required test cases:
    - Happy path
    - Validation failure
    - Unauthenticated access
    - Unauthorized access
    - Not found
    - Business rule failure
    - Edge cases
5. Propose the test plan and wait for approval.

### 2. Implement

After approval only:

1. Create Feature tests under the module or `tests/Feature` depending on project convention.
2. Create Unit tests under the module or `tests/Unit`.
3. Use descriptive `it()` descriptions.
4. Use Factories for test setup.
5. Use `actingAs()` where authentication is required.
6. Assert:
    - Correct status code
    - Unified response structure
    - Translated message when applicable
    - Response data shape
    - Database changes
    - Authorization behavior
7. Mock external services.
8. Avoid asserting internal implementation details.

### 3. Review

1. Run the relevant test filter first.
2. Run `php artisan test` when feasible.
3. Fix failing tests without weakening assertions.
4. Summarize:
    - Tests added
    - Scenarios covered
    - Commands run
    - Pass/fail result
    - Remaining gaps
