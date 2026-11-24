---
name: flutter-review-pr
description: >-
  Flutter Clean Architecture & S-S-W workflow: Review the current diff as a Senior Software Engineer before creating or submitting a pull request.
---

# Review PR

## Goal

Review the current diff as a Senior Software Engineer before creating or submitting a pull request.

## Mandatory Rules

- Do not modify files unless explicitly asked.
- Review against Clean Architecture, SOLID, Core Foundation First, S-S-W, Bloc standards, styling rules, and testing requirements.
- Be concise, technical, and actionable.
- Reject or flag changes that compromise maintainability, architecture, security, or testability.

## Workflow

### 1. Plan

1. Inspect the current git diff.
2. Identify changed files and affected features.
3. Categorize changes by layer:
   - `presentation`
   - `domain`
   - `data`
   - `core`
   - `test`
4. Determine whether the change introduces:
   - New UI
   - Logic changes
   - API/data changes
   - State management changes
   - Pagination
   - Animations
   - Destructive actions
   - New dependencies

### 2. Review Checklist

#### Architecture

- Verify feature structure follows:
  `lib/features/<feature>/[data, domain, presentation]`.
- Ensure domain remains pure and does not depend on data or presentation.
- Ensure repositories return direct entities or throw exceptions.
- Ensure no `Either` or `dartz` is introduced.
- Ensure data flow follows:
  UI → Bloc/Cubit → UseCase → Repository Interface → DataSource → ApiService.

#### Presentation

- Verify Screen-Section-Widget pattern.
- Screens must be stateless orchestration hubs only.
- Sections may contain BlocBuilder, BlocListener, navigation, dialogs, and Cubit calls.
- Widgets must be pure UI with no Bloc access or business logic.
- Ensure each class/widget lives in its own file.

#### State Management

- Verify all async operations use typed `StateStatus<T>`.
- Ensure status fields are descriptive, not generic `status`.
- Ensure UI uses `isLoading`, `isSuccess`, `isError`, not manual enum comparison.
- Ensure Bloc/Cubit catches only `ServerException`.
- Ensure controllers and form keys live inside Bloc/Cubit, not UI.
- Ensure initial fetching uses cascade operator in `BlocProvider.create`.

#### Data Layer

- Verify all endpoints are in `ApiConstants`.
- Verify all HTTP calls use `ApiService`.
- Verify DataSources use the double implementation pattern:
  - Interface
  - Real implementation
  - Fake implementation
- Ensure fake implementation uses `fakeFunction`.
- Ensure real implementation has no debug/fake logic.
- Ensure DTO to Entity mapping uses mapper extensions.

#### UI Styling

- Ensure no raw `Colors.xxx`.
- Use context color extensions.
- Use `CustomText`, `CustomButton`, `CustomTextField`, and project widgets where available.
- Use `.ph`, `.pw`, `.wi()`, `.he()`, `.rad()`, `.sp()`.
- Use `.onTap()` for custom taps.
- Ensure hardcoded strings are moved to `StringsManager`.

#### Testing

- Verify Unit, Bloc, and Widget tests are added or updated.
- Verify tests mirror the `lib/` folder structure.
- Verify success, failure, and edge cases are covered.
- Verify affected tests pass.

### 3. Output Format

Return the review using this structure:

```md
## PR Review

### Critical Issues

- ...

### Architecture Issues

- ...

### Testing Gaps

- ...

### UI / Styling Issues

- ...

### Maintainability Suggestions

- ...

### Security / Risk Notes

- ...

### PR Readiness

Score: X/10

### Recommended Next Steps

1. ...
2. ...
```
