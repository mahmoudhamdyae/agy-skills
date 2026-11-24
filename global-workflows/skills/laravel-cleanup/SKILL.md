---
name: laravel-cleanup
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Clean low-risk Laravel/PHP code quality issues while preserving behavior.
---

# Laravel Cleanup

## Goal

Clean low-risk Laravel/PHP code quality issues while preserving behavior.

## Mandatory Rules

- Follow Plan → Implement → Review.
- Wait for approval before editing files.
- Do not change behavior.
- Do not introduce new dependencies.
- Keep the footprint minimal.
- Respect existing patterns.

## Workflow

### 1. Plan

1. Inspect selected files or current diff.
2. Identify safe cleanup opportunities:
    - Unused imports
    - Missing type hints
    - Missing return types
    - Non-PSR-12 formatting
    - Inline FQCN usage
    - Duplicated small logic
    - Long methods
    - Debug statements
    - `env()` usage outside config
    - Direct `app()` or `resolve()` in business logic
    - Hardcoded strings that should be translated
    - Raw model returns in API
3. Separate safe cleanup from risky refactor.
4. Propose cleanup plan and wait for approval.

### 2. Implement

After approval only:

1. Remove unused imports.
2. Add strict parameter and return types.
3. Replace inline FQCN with imports.
4. Remove debug statements.
5. Replace `env()` outside config with `config()`.
6. Extract duplicated logic where safe.
7. Improve naming where safe.
8. Preserve behavior and response shape.

### 3. Review

1. Run formatter if configured.
2. Run affected tests.
3. Verify no behavior changed.
4. Summarize:
    - Cleanup performed
    - Files changed
    - Tests/checks run
    - Remaining cleanup opportunities
