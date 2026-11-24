---
trigger: model_decision
description: "Flutter Architecture Rule: 07_core_widgets_design_system.md"
---

# 07. Core Widgets and Design System

This document defines the mandatory core widgets in `lib/core/widgets/` to maintain visual consistency.

---

## 1. General Principles
- **Project Widgets First**: Never use standard Flutter widgets (Text, ElevatedButton, etc.) if a project-specific version exists.
- **Widgets > Functions**: Always prefer a separate widget class over a function returning a widget.
- **Single File**: Each widget must reside in its own separate file.

---

## 2. Widget Categories

### Typography (`texts/`)
- **`CustomText`**: The standard for all text. Supports auto-sizing and project styles.
- **`CustomRichText` / `CustomLangText`**: For mixed styles or auto-translated strings.

### Actions (`buttons/`)
- **`CustomButton`**: Primary button. Supports `.outlined()` and auto-translation.
- **`CustomTextButton` / `AppBackButton`**: For flat interactions and navigation.

### Input Fields (`text_field/`)
- **`CustomTextField`**: Base input with auto-validation.
- **Specialized**: `EmailTextField`, `PasswordTextField`, `PhoneTextField`, `SearchTextField`, `CustomPinCodeTextField`.
- **Pickers**: `CustomDatePicker`, `CustomMediaPicker`, `CustomLocationPicker`.

### Loading States (`custom_loading.dart`)
- **`Skeletonizer`**: (MANDATORY) Use for screen/list loading shimmers.
- **`FetchLoading` / `SubmitLoading`**: For data fetching or form submissions.
- **`InlineLoading` / `OverlayLoading`**: For small inline status or full-screen overlays.

### States & Feedback (`states_screens/`)
**MANDATORY**: Use these to handle `StateStatus` transitions.
- **`StatesScreen`**: For single-object views.
- **`StatesScreenList<T>` / `StatesScreenGrid<T>`**: For infinite scrolling logic.
    - MUST pass `cubit.paginationController`.
    - MUST provide `loadingWidget` and `loadingItems` for Skeletonizer.

### Dialogs (`dialogs/`)
- **`LoadingDialog` / `SuccessDialog` / `ErrorDialog`**: Standard feedback popups.
- **`DelDialog` / `SignOutDialog`**: (MANDATORY) Use for confirming destructive actions.

---

## 3. Specialized Layouts
- **`CustomScaffold` / `CustomAppBar`**: Standard structural wrappers.
- **`CustomRefreshIndicator`**: Standard pull-to-refresh.
- **`CustomWebViewScreen` / `ScannerWidget`**: For specialized feature needs.

---

## 4. Validation (`lib/core/validator/`)
Use `ValidateOperations` for all inputs:
- `normalValidation`, `emailValidation`, `phoneValidation`, `passwordValidation`.
