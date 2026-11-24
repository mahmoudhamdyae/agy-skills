---
name: add-api-endpoint
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Add or update a Laravel API endpoint using Clean Architecture, Form Requests, Services, Repositories, API Resources, unified responses, tests, and documentation.
---

# Add API Endpoint

## Goal

Add or update a Laravel API endpoint using Clean Architecture, Form Requests, Services, Repositories, API Resources, unified responses, tests, and documentation.

## Mandatory Rules

- Follow Plan → Implement → Review.
- Wait for approval before editing files.
- API routes must be versioned under `/api/v1/...`.
- Controllers must remain thin.
- Validation must be inside a Form Request.
- Never use `$request->validate()` or `Validator::make()` in Controllers or Services.
- Use API Resources for JSON responses.
- Never return raw models.
- All responses must follow the unified response structure:
    - `success`
    - `message`
    - `data`
- Messages must be translated.
- Repositories handle Eloquent/DB queries.
- Services handle business logic.
- Add Pest tests for happy path, validation failure, unauthenticated, unauthorized, and not found cases.
- Update `documentations/{phase}/api.md`.
- Update `documentations/{phase}/api_collection.json`.

## Workflow

### 1. Plan

1. Understand the endpoint purpose.
2. Identify:
    - HTTP method
    - URL
    - Middleware
    - Authorization requirements
    - Request payload
    - Response payload
    - Status codes
3. Inspect similar endpoints and module patterns.
4. Identify required files:
    - Route
    - Controller
    - Form Request
    - API Resource
    - Service
    - Repository
    - Contract if needed
    - Policy if needed
    - Tests
    - Documentation
    - Postman collection
5. State assumptions clearly.
6. Propose implementation steps and wait for approval.

### 2. Implement

After approval only:

1. Add or update the versioned API route.
2. Apply middleware at the route group level.
3. Create or update the Form Request.
4. Put all validation rules inside the Form Request.
5. Create or update the Controller with only:
    - Request receiving
    - Service call
    - Resource response
6. Create or update Service logic.
7. Create or update Repository queries.
8. Use constructor dependency injection.
9. Avoid `new ClassName()`, `app()`, or `resolve()` in business logic.
10. Create or update API Resource.
11. Trim response data to frontend needs only.
12. Use translated response messages.
13. Return correct HTTP status codes.
14. Update documentation and Postman collection.

### 3. Review

1. Add or update Pest Feature tests:
    - Happy path
    - Validation failure
    - Unauthenticated access
    - Unauthorized access
    - Not found case
2. Add or update Unit tests for Service and Repository when applicable.
3. Run `php artisan test`.
4. Verify the endpoint follows the unified response format.
5. Verify documentation and Postman collection match implementation.
6. Summarize:
    - Endpoint added/updated
    - Files changed
    - Tests added
    - Documentation updated
    - Verification result
