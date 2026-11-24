---
trigger: model_decision
description: "Flutter Architecture Rule: 03_ui_architecture_patterns.md"
---

# 03. UI Architecture Patterns (S-S-W)

This document defines the **Screen-Section-Widget (S-S-W)** pattern for building user interfaces.

---

## 1. The S-S-W Layers

| Layer | Responsibility | State Management | Logic & Interaction |
| :--- | :--- | :--- | :--- |
| **Screen** | Orchestration & Provider Hub | **None** (Stateless) | No business logic. |
| **Section** | Layout Grouping & Interaction | **BlocBuilder/Listener** | Navigation, Dialogs, Cubit calls. |
| **Widget** | Pure UI Presentation | **None** | Callbacks only (onTap, onChanged). |

### I. Screen (`.../presentation/screens/`)
- **Stateless by Default**: MUST be `StatelessWidget`.
- **Single Duty**: Contains `CustomScaffold` and calls **Sections**.
- **No Rendering Logic**: Strictly no `BlocBuilder` in the `build` method.

### II. Section (`.../presentation/sections/`)
- **Logic Hub**: All business logic and Cubit interactions reside here.
- **Section Nesting**: A Section can call another Section for complex sub-layouts.
- **Single File**: NEVER place multiple classes or widgets in the same file.

### III. Widget (`.../presentation/widgets/` or `lib/core/widgets/`)
- **UI Only**: ZERO business logic or direct Bloc access.
- **Data via Parameters**: Receives all data via constructors.
- **Widgets > Functions**: Always prefer `StatelessWidget` over helper functions.

---

## 2. Reusability & Performance

### Reusability Guide
- **Single Screen**: Place in `features/X/presentation/widgets/`.
- **Feature Wide**: Place in `features/X/presentation/widgets/`.
- **App Wide**: Move to `lib/core/widgets/`.

### Performance Rules
1. **Const Constructors**: Use `const` wherever possible.
2. **Pure Build**: Avoid heavy computations inside the `build` method.
3. **Spacing**: Use `num` extensions (`16.ph`, `12.pw`) instead of raw `SizedBox`.
4. **setState Caution**: Minimize `setState` usage; prefer granular Bloc updates.
