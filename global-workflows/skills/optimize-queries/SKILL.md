---
name: optimize-queries
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Review and optimize Eloquent queries for performance, readability, and scalability.
---

---

## 10. `optimize_queries.md`

```md
# Optimize Laravel Queries

## Goal

Review and optimize Eloquent queries for performance, readability, and scalability.

## Mandatory Rules

- Do not change behavior.
- Follow Plan → Implement → Review.
- Wait for approval before editing files.
- Avoid N+1 queries.
- Use eager loading.
- Use indexes for frequently filtered/sorted/joined columns.
- Use `select()` when full model payload is unnecessary.
- Use `chunk()`, `lazy()`, or `cursor()` for large datasets.
- Keep query logic inside Repositories where applicable.

## Workflow

### 1. Plan

1. Identify slow or risky queries.
2. Inspect Models, Repositories, Resources, and Controllers.
3. Look for:
    - N+1 relationship access
    - Missing eager loading
    - `all()` on large tables
    - Missing indexes
    - Over-fetching columns
    - Filtering in PHP instead of database
    - Expensive loops
4. Propose query optimization plan.
5. Wait for approval.

### 2. Implement

After approval only:

1. Move query logic to Repository if needed.
2. Add `with()` for relationships.
3. Use `select()` where safe.
4. Replace `all()` with paginated, chunked, lazy, or cursor-based retrieval.
5. Add scopes for repeated query conditions.
6. Suggest migration indexes if missing.
7. Avoid changing response shape unless explicitly approved.

### 3. Review

1. Verify response behavior remains unchanged.
2. Verify no N+1 issues remain.
3. Verify indexes support expected queries.
4. Add or update tests if query behavior affects output.
5. Summarize:
    - Query issues found
    - Optimizations applied
    - Potential indexes
    - Tests run
```
