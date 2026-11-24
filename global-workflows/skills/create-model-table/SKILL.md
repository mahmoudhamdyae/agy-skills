---
name: create-model-table
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Create a new model/table with migration, model, factory, seeder, relationships, casts, indexes, and tests according to Laravel database conventions.
---

# Create Model and Table

## Goal

Create a new model/table with migration, model, factory, seeder, relationships, casts, indexes, and tests according to Laravel database conventions.

## Mandatory Rules

- Follow Plan → Implement → Review.
- Wait for approval before creating files.
- Every new table/model must include:
    - Migration
    - Model
    - Factory
    - Seeder
- Register new Seeders.
- Use proper foreign keys, indexes, timestamps, and soft deletes.
- Define `$fillable` explicitly.
- Avoid `$guarded = []`.
- Define `$casts`.
- Define typed relationship methods.
- Add `scopeActive()` when the model has `is_active`.
- Use realistic fake data.

## Workflow

### 1. Plan

1. Understand the entity and its fields.
2. Identify relationships.
3. Identify whether fields are translatable.
4. Identify indexes based on:
    - WHERE
    - ORDER BY
    - JOIN
    - GROUP BY
5. Identify required casts:
    - boolean
    - datetime
    - enum
    - json
    - array
6. Identify whether soft deletes are required.
7. Propose migration and model structure.
8. Wait for approval.

### 2. Implement

After approval only:

1. Create migration.
2. Add:
    - `$table->id()`
    - Required fields
    - Foreign keys using `foreignId()->constrained()`
    - Indexes
    - `$table->timestamps()`
    - `$table->softDeletes()` for main entities
3. Create Model with:
    - `HasFactory`
    - `SoftDeletes` where applicable
    - `$fillable`
    - `$casts`
    - Typed relationships
    - Scopes
4. Create Factory with realistic fake data.
5. Create Seeder using the Factory.
6. Register Seeder in the correct seeder file.
7. Add tests if model behavior is significant.

### 3. Review

1. Verify migration rollback safety.
2. Verify indexes match expected queries.
3. Verify relationships are typed.
4. Verify Factory and Seeder work.
5. Run tests.
6. Summarize:
    - Table created
    - Model fields
    - Relationships
    - Indexes
    - Seeder/factory status
