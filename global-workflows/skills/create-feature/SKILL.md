---
name: create-feature
description: >-
  Flutter Clean Architecture & S-S-W workflow: Create a new feature using the project's mandatory Clean Architecture, S-S-W UI pattern, Bloc/Cubit state management, Core Foundation, fake data support, and testing architecture.
---

# Create Feature

## Goal

Create a new feature using the project's mandatory Clean Architecture, S-S-W UI pattern, Bloc/Cubit state management, Core Foundation, fake data support, and testing architecture.

## Mandatory Rules

- Follow Plan → Implement → Review.
- Wait for approval before creating files.
- Use the structure:
  `lib/features/<feature>/[data, domain, presentation]`
- Domain must remain pure.
- Presentation must not contain API or business logic.
- Data layer must contain DataSources, Models/DTOs, Repositories, and Mappers.
- Every Entity and Model must include `fake()` and `fakeList()` where applicable.
- Add Unit, Bloc, and Widget tests.
- Keep each class/widget/entity in its own file.

## Workflow

### 1. Plan

1. Understand the feature purpose and user flow.
2. Inspect similar existing features.
3. Propose the feature structure.
4. Identify:
   - Entities
   - Models/DTOs
   - UseCases
   - Repository interfaces
   - Repository implementations
   - DataSources
   - Mappers
   - Cubits/Blocs
   - Screens
   - Sections
   - Widgets
   - Tests
5. State assumptions clearly.
6. Wait for approval.

### 2. Implement

After approval only:

1. Create the domain layer.
2. Create the data layer.
3. Create the presentation layer using S-S-W.
4. Register dependencies.
5. Add fake data support.
6. Add tests mirroring the `lib/` structure.

### 3. Review

1. Run analyze and tests.
2. Verify architecture boundaries.
3. Verify 100% affected test pass rate.
4. Summarize implementation, tests, and assumptions.
