---
name: flutter-generate-tests
description: >-
  Flutter Clean Architecture & S-S-W workflow: Generate or update tests for the selected feature, file, Cubit/Bloc, UseCase, Repository, DataSource, Mapper, Section, or Widget while strictly following the project's testing architecture.
---

# Generate Tests

## Goal

Generate or update tests for the selected feature, file, Cubit/Bloc, UseCase, Repository, DataSource, Mapper, Section, or Widget while strictly following the project's testing architecture.

## Mandatory Rules

- Follow the project lifecycle: Plan → Implement → Review.
- Do not modify production code during the planning phase.
- Wait for approval before writing or changing files.
- Tests must mirror the `lib/` folder structure exactly.
- Use Unit, Bloc, and Widget tests where applicable.
- Use `.fake()` and `.fakeList()` from Entities and Models.
- Mock interfaces only, never concrete classes.
- Use `MockFallbacks.register()` in `setUpAll`.
- Use `bloc_test` for Cubit/Bloc tests.
- Use custom matchers such as `isLoadingStatus`, `isSuccessStatus`, and `isErrorStatus`.
- Use `pumpApp` for widget tests.
- Ensure all tests are deterministic, fast, and stable.
- End with verification that all relevant tests pass.

## Workflow

### 1. Plan

1. Inspect the selected file, folder, or feature.
2. Identify the exact architecture layer:
   - `data`
   - `domain`
   - `presentation`
   - `core`
3. Identify existing tests and project testing patterns.
4. Determine the required test types:
   - Unit tests for UseCases, Repositories, Mappers, Models, Utilities.
   - Bloc/Cubit tests for state transitions.
   - Widget tests for Sections and Widgets.
5. List the success, failure, and edge cases that must be covered.
6. Propose the test plan and wait for approval.

### 2. Implement

After approval only:

1. Create or update test files under the matching `test/` path.
2. Use existing fixtures, fake data, mocks, and matchers where available.
3. Add missing mocks only for interfaces.
4. Test successful flows.
5. Test failure flows, especially `ServerException`.
6. Test edge cases and empty states.
7. For widgets:
   - Use `pumpApp`.
   - Allow localization and animations to settle.
   - Avoid testing implementation details.

### 3. Review

1. Run the relevant tests.
2. Fix test issues without changing business logic unless a real bug is identified.
3. Verify 100% pass rate for the affected tests.
4. Summarize:
   - Added tests
   - Updated tests
   - Covered scenarios
   - Remaining risks or gaps
