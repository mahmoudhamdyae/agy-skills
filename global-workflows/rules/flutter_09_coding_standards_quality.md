---
trigger: model_decision
description: "Flutter Architecture Rule: 09_coding_standards_quality.md"
---

# 09. Coding Standards and Quality

This document defines the high-level quality standards and global coding principles.

---

## 1. THE GOLDEN RULE: Core Foundation First
If a utility, helper, extension, or manager exists in `lib/core/`, you **MUST** use it. **This is the most critical rule of the project.**

- **No Reinvention**: Never write one-off logic for features already handled by Core (e.g., Navigator, Dio, Spacing).
- **Files > Raw**: Always prefer project-specific extensions and managers over raw Flutter/Dart code.

---

## 2. Coding Standards (Effective Dart 2026)

### Naming Conventions:
- **PascalCase**: Classes, Enums, Extensions.
- **lowerCamelCase**: Variables, Functions, Constants (No `SCREAMING_SNAKE`).
- **snake_case**: File names, Directories, URIs.
- **Privacy (`_`)**: Mandatory leading underscore for private members.
- **Descriptive Names**: NEVER use `id` or `name` alone. Use `productId`, `categoryName`, etc.

### Core Principles:
- **Single File Principle**: (MANDATORY) Every class, widget, or entity MUST reside in its own separate file.
- **Explicit Typing**: (MANDATORY) Always specify types (e.g., `final int count = 0;`). Avoid `var` unless the type is redundant.
- **DRY & SOLID**: Avoid duplication. Each file/function must have a single responsibility.
- **Method Extraction**: Always extract non-trivial callbacks and repetitive UI logic out of the `build` function.

---

## 3. Performance & Logic

| Area | Mandatory Standard |
| :--- | :--- |
| **Widgets** | Use `const` constructors wherever possible. |
| **Logic** | Avoid heavy computations in `build()`. Use isolates or caching for heavy tasks. |
| **Interactions**| Use **`.onTap()`** extension or `GestureDetector` over `InkWell`. |
| **Confirmation**| (MANDATORY) Always require user confirmation before destructive actions (Delete, SignOut). |

---

## 4. Error Handling & Testing

### Error Propagation:
- **No Silent Failures**: Never let errors fail silently.
- **Try/Catch**: Handle `ServerException` directly in the Bloc/Cubit layer and emit an `.error()` state.
- **Exceptions > Either**: Do NOT use `Either` or `dartz`. Repositories return data directly or throw exceptions.

### Quality Assurance:
- **Mandatory Testing**: Every task MUST include corresponding tests (Unit, Bloc, Widget).
- **Pass Rate**: All tests must achieve a **100% pass rate** before code is considered ready.
- **Mirroring**: Test files MUST mirror the `lib/` directory structure exactly.
