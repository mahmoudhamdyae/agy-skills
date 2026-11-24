---
name: add-paginated-list
description: >-
  Flutter Clean Architecture & S-S-W workflow: Implement an infinite scrolling list or grid using the project's mandatory pagination architecture.
---

# Add Paginated List

## Goal

Implement an infinite scrolling list or grid using the project's mandatory pagination architecture.

## Mandatory Rules

- Follow Plan → Implement → Review.
- Wait for approval before changing files.
- Never deviate from the project pagination standard.
- Use `PaginatedResult<T>`.
- Use `.toPaginatedResult()`.
- Use `PaginationMixin<TState, TItem>`.
- Use `PaginationController`.
- Use `StatesScreenList<T>` or `StatesScreenGrid<T>`.
- Add or update tests.

## Workflow

### 1. Plan

1. Inspect the feature and existing pagination examples.
2. Identify the paginated entity type.
3. Identify API request parameters.
4. Identify response metadata shape.
5. Propose changes across:
   - Entity
   - Model/DTO
   - Mapper
   - DataSource
   - Repository
   - UseCase
   - Cubit
   - State
   - Section
   - Widget
   - Tests
6. Wait for approval.

### 2. Implement

After approval only:

1. Return `PaginatedResult<T>` from the domain/data flow.
2. Use `.toPaginatedResult()` in the mapper.
3. Add `PaginationMixin<TState, TItem>` to the Cubit.
4. Call `initPagination()` in the Cubit constructor.
5. Call `disposePagination()` in `close()`.
6. Implement `fetchPage(int page)`.
7. Implement `getItems({int page = 1, bool showLoading = true})`.
8. Use `StatesScreenList<T>` or `StatesScreenGrid<T>` in the Section.
9. Pass `cubit.paginationController`.
10. Provide fake loading items and Skeletonizer-compatible loading widgets.

### 3. Review

1. Test first page loading.
2. Test loading more pages.
3. Test empty state.
4. Test error state.
5. Test retry behavior.
6. Run affected tests.
7. Summarize verification result.
