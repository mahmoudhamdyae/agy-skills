---
name: laravel-review-pr
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Review the current diff as a Senior Laravel/PHP Software Engineer before submitting or merging a pull request.
---

# Review Laravel PR

## Goal

Review the current diff as a Senior Laravel/PHP Software Engineer before submitting or merging a pull request.

## Mandatory Rules

- Do not modify files unless explicitly asked.
- Review against Clean Architecture, SOLID, TDD, security, performance, modular architecture, Filament, localization, and documentation rules.
- Be concise, technical, and actionable.
- Flag changes that compromise maintainability, security, or testability.

## Workflow

### 1. Inspect

1. Read the current diff.
2. Identify changed modules and files.
3. Categorize changes:
    - API
    - Controller
    - Form Request
    - Resource
    - Service
    - Repository
    - Model
    - Migration
    - Factory
    - Seeder
    - Policy
    - Job
    - Event / Listener
    - Filament
    - Translation
    - Tests
    - Documentation

### 2. Review Checklist

#### Architecture

- Controllers are thin.
- Business logic is in Services.
- Query logic is in Repositories.
- Contracts are used where dependency inversion is needed.
- No direct cross-module tight coupling unless justified.
- Events/Listeners are used for decoupled side effects.
- Jobs are used for long-running tasks and external API calls.

#### API

- Routes are versioned under `/api/v1/...`.
- Middleware is applied at route group level.
- Request validation uses Form Requests only.
- Responses use API Resources.
- Response structure follows:
    - `success`
    - `message`
    - `data`
- Messages are translated.
- Response payload is trimmed to frontend needs.

#### Database

- Migrations use proper column types.
- Foreign keys use constrained pattern.
- Indexes exist for filtered, sorted, joined, or grouped columns.
- Main entities use soft deletes.
- Models define `$fillable`.
- Models define `$casts`.
- Relationships are typed.
- Factories and Seeders exist and are updated.

#### Eloquent Performance

- Queries avoid N+1 problems.
- `with()` is used for eager loading.
- `select()` is used when large payloads are unnecessary.
- Large dataset processing uses `chunk()`, `lazy()`, or `cursor()`.
- No unnecessary `all()` on large tables.

#### Security

- Authorization uses Policies or Gates.
- No authorization checks inside business logic.
- Passwords use `Hash::make()`.
- Sensitive data is not logged or returned.
- No raw SQL without bindings.
- Public endpoints have rate limiting.

#### Code Style

- PSR-12 is followed.
- Strict parameter and return types are used.
- Constructor property promotion is used where appropriate.
- `readonly` properties are used where appropriate.
- No FQCN usage inline; use imports.
- No `env()` outside config files.
- No `dd()`, `dump()`, `var_dump()`, or `print_r()`.

#### Testing

- Pest tests exist for every endpoint and business rule.
- Feature tests cover happy path, validation, unauthenticated, unauthorized, and not found cases.
- Unit tests cover Services and Repositories.
- Factories are used for data setup.
- External services are mocked.

#### Documentation

- Endpoint changes are reflected in `api.md`.
- Endpoint changes are reflected in `api_collection.json`.
- Documentation matches the actual response structure.

### 3. Output Format

```md
## PR Review

### Critical Issues

- ...

### Architecture Issues

- ...

### Security Issues

- ...

### Performance Issues

- ...

### Testing Gaps

- ...

### Documentation Gaps

- ...

### Maintainability Suggestions

- ...

### PR Readiness

Score: X/10

### Required Next Steps

1. ...
2. ...
```
