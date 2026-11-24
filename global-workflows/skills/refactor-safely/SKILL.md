---
name: refactor-safely
description: >-
  Flutter Clean Architecture & S-S-W workflow: Improve code readability, maintainability, and architecture alignment without changing behavior.
---

# Refactor Safely

## Goal

Improve code readability, maintainability, and architecture alignment without changing behavior.

## Mandatory Rules

- Do not change behavior unless explicitly approved.
- Follow Plan → Implement → Review.
- Wait for approval before editing files.
- Keep the footprint minimal.
- Preserve public APIs unless explicitly approved.
- Respect SOLID, Clean Architecture, S-S-W, and Core Foundation First.
- Update tests only when necessary to preserve behavior verification.

## Workflow

### 1. Plan

1. Inspect the selected file, folder, or feature.
2. Identify maintainability issues:
   - Duplicate logic
   - Large classes
   - Large build methods
   - Mixed responsibilities
   - Logic in UI widgets
   - Hardcoded strings
   - Raw Flutter widgets where project widgets exist
   - Raw navigation/dialog/snackbar usage
   - Non-standard spacing, colors, or typography
3. Identify the safest refactoring steps.
4. Confirm which behavior must remain unchanged.
5. Propose a minimal refactor plan and wait for approval.

### 2. Implement

After approval only:

1. Refactor incrementally.
2. Keep each class/widget/entity in its own file.
3. Extract non-trivial callbacks from `build`.
4. Replace helper functions returning widgets with separate `StatelessWidget` classes.
5. Move reusable UI to the correct location:
   - Feature-specific widgets under the feature.
   - App-wide widgets under `lib/core/widgets/`.
6. Use project-specific utilities:
   - `CustomText`
   - `CustomButton`
   - `CustomScaffold`
   - `CustomTextField`
   - `.ph`, `.pw`
   - `.wi()`, `.he()`, `.rad()`, `.sp()`
   - `.onTap()`
   - Context theme extensions
7. Preserve all current behavior.

### 3. Review

1. Run relevant tests.
2. Verify no behavior changed.
3. Verify improved readability and architectural alignment.
4. Summarize:
   - Refactoring performed
   - Behavior preserved
   - Tests run
   - Any remaining refactor opportunities
