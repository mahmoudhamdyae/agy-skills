---
name: migration-check
description: >-
  Flutter Clean Architecture & S-S-W workflow: Review database, API, model, DTO, or state migration changes for safety, compatibility, and maintainability.
---

# Migration Check

## Goal

Review database, API, model, DTO, or state migration changes for safety, compatibility, and maintainability.

## Mandatory Rules

- Do not apply or modify migrations unless explicitly asked.
- Identify destructive or breaking changes.
- Preserve backward compatibility where possible.
- Add or update tests for parsing, mapping, and affected business logic.
- Use project-safe parsing and architecture patterns.

## Workflow

### 1. Plan

1. Inspect the migration or changed data model.
2. Identify what is changing:
   - Field added
   - Field removed
   - Field renamed
   - Type changed
   - Nullability changed
   - Enum changed
   - Response shape changed
   - Pagination shape changed
3. Identify affected layers:
   - Model/DTO
   - Mapper
   - Entity
   - UseCase
   - Repository
   - Cubit/Bloc
   - UI
   - Tests

### 2. Review Checklist

1. Verify DTO parsing uses `ParseUtils`.
2. Verify removed or renamed fields do not break existing mapping.
3. Verify nullable fields are handled safely.
4. Verify Entities and Models still include `fake()` and `fakeList()`.
5. Verify mappers still return correct Domain Entities.
6. Verify Repository return types remain direct entities.
7. Verify Cubit/Bloc status types are still correct.
8. Verify UI handles empty, loading, success, and error states.
9. Verify pagination still uses `PaginatedResult<T>` where applicable.
10. Verify tests cover old and new response shapes if needed.

### 3. Output Format

```md
## Migration Review

### Breaking Risks

- ...

### Compatibility Notes

- ...

### Required Code Updates

- ...

### Required Test Updates

- ...

### Safe Rollout Recommendation

- ...

### Final Recommendation

Proceed / Block / Proceed after fixes
```
