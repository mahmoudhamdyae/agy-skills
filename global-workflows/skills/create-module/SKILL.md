---
name: create-module
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Create a new Laravel module using nWidart/laravel-modules while following Clean Architecture, SOLID, TDD, Filament, localization, and documentation standards.
---

# Create Laravel Module

## Goal

Create a new Laravel module using nWidart/laravel-modules while following Clean Architecture, SOLID, TDD, Filament, localization, and documentation standards.

## Mandatory Rules

- Follow Plan → Implement → Review.
- Do not create files before approval.
- Use nWidArt module structure under `Modules/{ModuleName}`.
- Keep the module self-contained.
- Use Services for business logic.
- Use Repositories for Eloquent/DB queries.
- Use Contracts when dependency inversion is needed.
- Do not query Eloquent directly inside Controllers or Services when a Repository is appropriate.
- Add bilingual translations for Arabic and English.
- Add tests for all API endpoints and service logic.
- Update documentation and Postman collection when endpoints are added.

## Workflow

### 1. Plan

1. Understand the module purpose and business domain.
2. Inspect similar existing modules before proposing structure.
3. Identify required:
    - Models
    - Migrations
    - Factories
    - Seeders
    - Controllers
    - Form Requests
    - API Resources
    - Services
    - Repositories
    - Contracts
    - Policies
    - Events / Listeners / Jobs
    - Filament Resources
    - Translation files
    - Tests
    - Documentation files
4. Propose the module structure.
5. Explain architectural trade-offs.
6. State assumptions clearly.
7. Wait for approval before implementation.

### 2. Implement

After approval only:

1. Create the module using the project’s nWidart convention.
2. Create module folders according to the standard structure.
3. Add `lang/ar` and `lang/en` files.
4. Add Models with:
    - `$fillable`
    - `$casts`
    - Typed relationships
    - `SoftDeletes` for main entities
    - `scopeActive()` when `is_active` exists
5. Add migrations with:
    - Proper column types
    - Foreign keys
    - Indexes
    - Timestamps
    - Soft deletes
6. Add Factories with realistic fake data.
7. Add Seeders and register them in the module seeder.
8. Add Services and Repositories.
9. Add Contracts where cross-module or complex dependencies exist.
10. Add API routes under `/api/v1/...`.
11. Add Filament resources inside the module if needed.
12. Add tests using Pest.
13. Add or update API documentation and Postman collection.

### 3. Review

1. Run formatting and tests.
2. Verify Clean Architecture boundaries.
3. Verify module isolation.
4. Verify translations exist for Arabic and English.
5. Verify API documentation is synced.
6. Summarize:
    - Files created
    - Architecture decisions
    - Tests added
    - Documentation updated
    - Remaining assumptions
