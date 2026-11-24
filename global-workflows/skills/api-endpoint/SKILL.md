---
name: api-endpoint
description: >-
  Flutter Clean Architecture & S-S-W workflow: Add a new API endpoint or integrate an existing backend endpoint using the project's Clean Architecture and networking standards.
---

---

## 7. `api_endpoint.md`

```md
# Add API Endpoint

## Goal

Add a new API endpoint or integrate an existing backend endpoint using the project's Clean Architecture and networking standards.

## Mandatory Rules

- Follow Plan → Implement → Review.
- Wait for approval before changing files.
- Use `ApiService` for all HTTP requests.
- Put all endpoints in `ApiConstants`.
- Repositories return entities directly.
- Do not use `Either` or `dartz`.
- Use DataSource double implementation.
- Add or update Unit, Bloc, and Widget tests where applicable.
- Keep production and fake implementations separate.

## Workflow

### 1. Plan

1. Understand the endpoint purpose, method, request body, query params, and response shape.
2. Inspect existing endpoints and feature patterns.
3. Identify affected layers:
   - `domain/entities`
   - `domain/repositories`
   - `domain/usecases`
   - `data/models`
   - `data/datasources`
   - `data/repositories`
   - `data/mappers`
   - `presentation/blocs`
   - `presentation/sections`
   - `presentation/widgets`
4. Propose the file list and implementation plan.
5. State assumptions about request/response if backend docs are incomplete.
6. Wait for approval.

### 2. Implement

After approval only:

#### Domain

1. Add or update Entity with:
   - `static fake()`
   - `static fakeList()` when applicable
2. Add or update Repository interface.
3. Add or update UseCase returning `Future<T>` directly.

#### Data

1. Add endpoint to `ApiConstants`.
2. Add or update DTO/Model with:
   - Safe parsing using `ParseUtils`
   - `static fake()`
   - `static fakeList()` when applicable
3. Add mapper extension:
   - `toModel()` for single objects
   - `toModelList()` for lists
4. Add or update DataSource interface.
5. Add or update real DataSource implementation using `ApiService`.
6. Add or update fake DataSource implementation using `fakeFunction`.
7. Add or update Repository implementation.

#### Presentation

1. Add or update Cubit/Bloc event/method.
2. Use typed descriptive `StateStatus<T>`.
3. Use `.loading()`, `.success(data)`, and `.error(message)`.
4. Catch only `ServerException`.
5. Add optional `showLoading = true` for async methods.
6. Use Sections for Bloc interaction and UI state handling.
7. Use Widgets only for pure UI.

#### DI

1. Register dependencies.
2. Use `ConstantsManager.isDebug` to choose fake or real DataSource.
3. Do not put debug checks inside the real implementation.

### 3. Review

1. Add/update tests for:
   - Model parsing
   - Mapper
   - UseCase
   - Repository
   - DataSource interface behavior
   - Cubit/Bloc state transitions
   - Widget/Section behavior if UI changed
2. Run affected tests.
3. Verify 100% pass rate.
4. Summarize:
   - Endpoint added
   - Layers changed
   - Tests added
   - Assumptions
   - Verification result
```
