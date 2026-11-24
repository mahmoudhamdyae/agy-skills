---
trigger: model_decision
description: "Flutter Architecture Rule: 06_ui_styling_theming_responsive.md"
---

# 06. UI Styling, Theming, and Responsive Design

This document defines visual consistency, dark mode support, and responsive layouts.

---

## 1. Responsive Design (`390 × 844` Baseline)

| Extension | Purpose | Example |
| :--- | :--- | :--- |
| **`wi()`** | Width scaling | `100.wi()` |
| **`he()`** | Height scaling | `200.he()` |
| **`rad()`** | BorderRadius scaling | `12.rad()` |
| **`sp()`** | FontSize scaling | `14.sp()` |

### Adaptive Layouts:
- **`getValueForScreenType`**: Use for values that change between phone/tablet/desktop.
- **Rules**: Never use standard suffixes (`.w`, `.h`). Always use project custom extensions.

---

## 2. Spacing and Layout

| Extension | Widget Equivalent | Usage |
| :--- | :--- | :--- |
| **`.ph`** | `SizedBox(height: ...he())` | `16.ph` |
| **`.pw`** | `SizedBox(width: ...wi())` | `12.pw` |
| **`.sliverPh`** | `SliverToBoxAdapter` (Vertical) | `16.sliverPh` |
| **`.sliverPw`** | `SliverToBoxAdapter` (Horizontal) | `12.sliverPw` |

---

## 3. Theming & Dark Mode (Context Extensions)
**MANDATORY**: Never use static colors or `Colors.xxx`. Always use `context` extensions.

| Type | Extension | Usage |
| :--- | :--- | :--- |
| **Colors** | `context.primaryColor` | `color: context.primaryColor` |
| **Scheme** | `context.colorScheme.surface` | `color: context.colorScheme.surface` |
| **Opacity** | `withValues(alpha: ...)` | `color.withValues(alpha: .2)` |

---

## 4. Typography (Chainable Styles)
**MANDATORY**: Use `context.textTheme` as base, then chain modifiers.

- **Base Styles**: `context.displayLarge`, `context.titleLarge`, `context.bodyMedium`.
- **Modifiers**:
    - **Color**: `.primary`, `.text1`, `.white`, `.withColor(color)`.
    - **Size**: `.s12`, `.s16`, `.s24`, `.withSize(15)`.
    - **Weight**: `.regular`, `.medium`, `.semiBold`, `.bold`, `.black`.

---

## 5. Widget Helpers and Interaction
Chain these helpers from `core/extensions/widget_extensions.dart`.

- **Padding**: `.paddingAll(16)`, `.paddingHorizontal(24)`.
- **Sizing**: `.withHeight(200.he())`, `.withWidth(100.wi())`.
- **Layout**: `.expand()`, `.flexible()`, `.center()`, `.visible(bool)`.
- **Interaction**: **`.onTap(() {})`** (MANDATORY for custom taps over `GestureDetector`).
- **Decorations**: `.cornerRadiusWithClipRRect(12)`, `.form(formKey)`.
