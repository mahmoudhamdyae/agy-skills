---
trigger: model_decision
description: "Flutter Architecture Rule: 04_state_management_bloc.md"
---

# 04. State Management with BLoc and StateStatus

This document defines how to manage the application state using `flutter_bloc` and the `StateStatus<T>` utility.

---

## 1. The `StateStatus<T>` Utility
Located in `core/base/state_status.dart`. This is **MANDATORY** for all asynchronous operations in a Bloc/Cubit state.

| Method | When to Use | Example Emission |
| :--- | :--- | :--- |
| **`.initial()`** | BLoc creation or form reset. | `emit(state.copyWith(status: .initial()));` |
| **`.loading()`** | Before starting an async operation. | `emit(state.copyWith(status: .loading()));` |
| **`.success(T data)`** | Async operation completes successfully. | `emit(state.copyWith(status: .success(result)));` |
| **`.error(String)`** | Case of `ServerException` or failure. | `emit(state.copyWith(status: .error(message)));` |

---

## 2. UI Integration (The S-S-W Standard)

### Reading State
Always use the built-in boolean getters (`isSuccess`, `isLoading`, etc.). **Never** compare the `status` enum manually.

```dart
BlocBuilder<MyBloc, MyState>(
  buildWhen: (previous, current) => previous.jobStatus != current.jobStatus,
  builder: (context, state) {
    if (state.jobStatus.isLoading) return const FetchLoading();
    if (state.jobStatus.isSuccess) return SuccessWidget(data: state.jobStatus.data!);
    return const SizedBox.shrink();
  },
)
```

### Key UI Containers
- **`StatesScreen` wrappers**: Use `StatesScreen`, `StatesScreenList`, or `StatesScreenGrid` for full-screen or large section state handling. They automate loading, error, and empty states.

---

## 3. Mandatory Developer Rules

### Architecture & Naming
- **Descriptive Status**: (MANDATORY) Never use generic names like `status`. Use `getProductsStatus`, `deleteUserStatus`, etc.
- **Explicit Typing**: (MANDATORY) Always type `StateStatus` (e.g., `StateStatus<UserEntity>`, `StateStatus<void>`).
- **Initial Fetching**: (MANDATORY) Use the cascade operator `..` in `BlocProvider.create` (e.g., `..getData()`) instead of `initState`.

### Code Structure
- **Single File**: (MANDATORY) Bloc, State, and Event/Status classes must each reside in their own separate file.
- **Controllers**: (MANDATORY) All `TextEditingController` and `GlobalKey<FormState>` MUST be managed inside the **Bloc/Cubit**, not the UI.
- **Data Methods**: Every state/event needs a `<editor-fold desc="Data Methods">` containing a `const constructor`, `==/hashCode`, `toString`, and `copyWith`.

### Shorthand & Logic
- **Shorthand Syntax**: (MANDATORY) Use inferred shorthands (e.g., `.initial()`, `crossAxisAlignment: .start`).
- **Validation**: (MANDATORY) Use `formState.validateAndScroll()` for forms.
- **Loading Control**: Async events must have an optional `showLoading` boolean (default `true`) to control status emission.
- **Try/Catch**: Blocs catch **only** `ServerException`.
