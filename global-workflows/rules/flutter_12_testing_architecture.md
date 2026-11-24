---
trigger: model_decision
description: "Flutter Architecture Rule: 12_testing_architecture.md"
---

# 12. Testing Architecture and Conventions

This document defines the testing standards. Follow it exactly to ensure reproducible test structures.

---

## 1. The Mandatory Testing Rule
- **New Features**: MUST be developed with Unit, Bloc, and Widget tests.
- **Modifications**: MUST include updates to relevant tests to prevent regressions.
- **Coverage**: Coverage must include success, failure, and edge cases for all layers.

---

## 2. Mirror Folder Architecture
**MANDATORY**: The `test/` directory MUST mirror the `lib/` directory structure exactly.

- `test/core/`: Shared infrastructure (helpers, matchers, mocks).
- `test/features/<feature>/`:
    - `data/`: Models, DTOs, Mappers, Repositories.
    - `domain/`: Use Cases.
    - `presentation/`: Blocs, Sections, Widgets.
- `integration_test/`: End-to-end flows mirroring the `features` structure.

---

## 3. Testing Standards

### Widget Testing (`pumpApp`)
Always use the `pumpApp` extension to wrap widgets in the required environment.
- **Platform Mocks**: `pumpApp` MUST mock channels (e.g., `url_launcher`, `path_provider`) to prevent crashes.
- **Stabilization**: Always use `runAsync` with a **500ms delay** to allow `EasyLocalization` and animations to settle.

### Bloc/Cubit Testing
Use `bloc_test` and custom matchers from `test/core/matchers/`.
- **Matchers**: Use `isLoadingStatus`, `isSuccessStatus`, `isErrorStatus`.
- **Logic**: Verify every state transition in the `expect` block.

### Mocking (Mocktail)
- **Interfaces Only**: Always mock repository/datasource interfaces, never concrete classes.
- **Fallbacks**: (MANDATORY) Call `MockFallbacks.register()` in `setUpAll`.
- **Fixtures**: Use `.fake()` and `.fakeList()` from Entities/Models for mock data.

---

## 4. Core Expectations
- **100% Pass Rate**: Every task MUST end with verification that all tests pass.
- **Refactoring**: If refactoring breaks tests, you MUST update them while preserving business logic verification.
- **Fast & Stable**: Tests must be deterministic and execute quickly.
