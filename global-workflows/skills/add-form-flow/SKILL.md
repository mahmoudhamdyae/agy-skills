---
name: add-form-flow
description: >-
  Flutter Clean Architecture & S-S-W workflow: Create or update a form flow using the project's Bloc/Cubit, validation, styling, and UI architecture standards.
---

# Add Form Flow

## Goal

Create or update a form flow using the project's Bloc/Cubit, validation, styling, and UI architecture standards.

## Mandatory Rules

- Follow Plan → Implement → Review.
- Wait for approval before changing files.
- Manage `TextEditingController` and `GlobalKey<FormState>` inside Bloc/Cubit.
- Use `validateAndScroll()` for validation.
- Use `HelperFunctions.unFocusKeyboard()` on submit.
- Use project text fields and validators.
- Use typed descriptive `StateStatus<T>`.
- Add Bloc and Widget tests.

## Workflow

### 1. Plan

1. Inspect similar form flows.
2. Identify fields, validators, submit action, and success/error behavior.
3. Identify required state fields and controllers.
4. Identify whether the form triggers:
   - API mutation
   - Local state update
   - Navigation
   - Dialog
   - Snackbar
5. Propose implementation plan and wait for approval.

### 2. Implement

After approval only:

1. Add controllers and form key inside Cubit/Bloc.
2. Add descriptive typed submit status.
3. Add submit method with `showLoading = true`.
4. Call `validateAndScroll()`.
5. Call `HelperFunctions.unFocusKeyboard()`.
6. Call UseCase from Cubit/Bloc.
7. Catch only `ServerException`.
8. Emit `.loading()`, `.success(data)`, and `.error(message)`.
9. Build UI using:
   - Screen as orchestration only.
   - Section for Bloc interaction.
   - Widgets for pure UI.
10. Use project fields:

- `CustomTextField`
- `EmailTextField`
- `PasswordTextField`
- `PhoneTextField`

11. Use `CustomButton` for submission.
12. Use project styling and spacing extensions.

### 3. Review

1. Add or update Bloc tests for:
   - Initial state
   - Validation failure
   - Loading
   - Success
   - ServerException error
2. Add widget tests for:
   - Required fields
   - Submit button
   - Loading state
   - Error state
3. Run affected tests.
4. Summarize result.
