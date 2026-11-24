---
name: connect-design-to-apis
description: >-
  Flutter Clean Architecture & S-S-W workflow: Connect an already implemented Flutter design/screen to backend APIs while preserving UI and following Clean Architecture, S-S-W, Bloc/Cubit, `StateStatus<T>`, Core Foundation, and tests.
---

# Connect Existing Flutter Design to APIs

## Goal

Connect an already implemented Flutter design/screen to backend APIs while preserving UI and following Clean Architecture, S-S-W, Bloc/Cubit, `StateStatus<T>`, Core Foundation, and tests.

Use when the user provides API details, Swagger/OpenAPI, Postman, request/response samples, or endpoint docs and wants an existing design wired to real data.

## Inputs

- API endpoint(s): method, URL, headers, params, body, success/error responses, auth.
- Target feature/screen.
- Whether API replaces fake/static data or adds an interaction.
  If missing, inspect code first. Ask one short question only if unsafe.

## Mandatory Rules

- Plan → Implement → Review.
- Do not edit before approval.
- Preserve existing design unless state UI is required.
- Architecture: UI → Bloc/Cubit → UseCase → Repository interface → Repository impl → DataSource → `ApiService`.
- Presentation has no API/business logic.
- Repositories return entities directly; no `Either`/`dartz`.
- Bloc/Cubit catches only `ServerException`.
- Async state uses typed descriptive `StateStatus<T>`, never generic `status`.
- Use S-S-W: Screen orchestration, Section state/interactions, Widget pure UI.
- Add/update tests.

## Related Workflows

Use as needed:

- `/api_endpoint`
- `/migration_check`
- `/add_form_flow`
- `/add_paginated_list`
- `/generate_tests`
- `/fix_bug`
- `/review_pr`
- `/cleanup`

## Routing

- Static/fake UI → API-backed: `/api_endpoint` → `/generate_tests` → `/review_pr`
- API response changed/unclear: `/migration_check` → `/api_endpoint` → `/generate_tests` → `/review_pr`
- Form submit API: `/add_form_flow` → `/api_endpoint` → `/generate_tests` → `/review_pr`
- Paginated API: `/api_endpoint` → `/add_paginated_list` → `/generate_tests` → `/review_pr`
- Broken after API connection: `/fix_bug` → `/migration_check` if needed → `/generate_tests` → `/review_pr`

## 1. Plan

1. Read API details.
2. Identify target feature/screen.
3. Inspect existing Screen, Sections, Widgets, Cubit/Bloc, fake data, entities/models, and similar API patterns.
4. Classify API:
   - single object
   - list
   - paginated list
   - form submit
   - mutation
   - upload
   - search/filter/sort
5. List required files:
   - Entity
   - Model/DTO
   - Mapper
   - DataSource interface
   - Real/Fake DataSource impl
   - Repository interface/impl
   - UseCase
   - Cubit/Bloc method or event
   - State field
   - Section wiring
   - Widget params/callbacks
   - Tests
6. Check existing UI states: loading, empty, error, success, submit loading.
7. Output plan and wait for approval.

Use output:

```md
## API Connection Plan

### Target Feature

...

### Target Screen(s)

...

### API Type

Fetch / Mutation / Form Submit / Paginated List / Upload / Search

### Required Workflow(s)

1. ...

### Files Likely to Change

- ...

### Assumptions

- ...

### Approval Needed

Yes
```

## 2. Normalize API Contract

Document before coding:

````md
## API Contract

### Endpoint

METHOD /path

### Headers

- ...

### Query / Path Parameters

- ...

### Request Body

```json
{}
```
````

### Success Response

```json
{}
```

### Error Response

```json
{}
```

### Auth

Required / Not required / Unknown

````
If contract is incomplete, infer only from similar endpoints when safe; otherwise ask.

## 3. Data Layer
Use `/api_endpoint`.

### ApiConstants
- Put endpoint paths in `ApiConstants`.
- No hardcoded endpoint strings in DataSources.

### Model/DTO
- Match API fields.
- Use safe parsing conventions.
- Add `static fake()` and `static fakeList()` when applicable.
- Do not leak DTOs to presentation.

### Entity
- Domain-only data needed by UI/business logic.
- Add `fake()` / `fakeList()` when applicable.
- Avoid backend metadata unless UI needs it.

### Mapper
- Create/update mapper extension in `data/mappers/`.
- Use `toModel()` and `toModelList()`.
- Handle nullable/optional fields safely.

### DataSource
Create/update:
- Interface
- Real impl using `ApiService`
- Fake impl using `fakeFunction`
Real impl uses correct `ApiService` method: `get`, `getList`, `getObject`, `post`, `put`, `delete`.
Use `showLoading: true` for POST/PUT/DELETE when global overlay is appropriate.
Never put fake/debug logic in real impl.

### Repository
- Interface in domain, impl in data.
- Returns entities directly.
- Maps DTO/Model → Entity.
- No `Either`/`dartz`.

### UseCase
- Return `Future<T>` directly.
- Keep focused and small.

## 4. State Management
1. Add/update Cubit/Bloc method/event.
2. Use typed descriptive statuses:
```dart
final StateStatus<UserProfileEntity> getUserProfileStatus;
final StateStatus<List<ProductEntity>> getProductsStatus;
final StateStatus<void> updateProfileStatus;
````

3. Async methods support `bool showLoading = true`.
4. Emit `.loading()`, `.success(data)`, `.error(message)`.
5. Catch only `ServerException`.
6. Initial fetch uses cascade in `BlocProvider.create`: `..getData()`.
7. Controllers/FormKeys live in Cubit/Bloc, not UI.

## 5. Connect UI

### Screen

- Orchestration only.
- Use `CustomScaffold`.
- Provide Cubit/Bloc if needed.
- No business logic or direct `BlocBuilder` in Screen build.

### Section

- Add `BlocBuilder`, `BlocListener`, or `BlocConsumer`.
- Use `buildWhen`/`listenWhen`.
- Use `isLoading`, `isSuccess`, `isError`; no manual enum comparison.
- Use `StatesScreen`, `StatesScreenList`, or `StatesScreenGrid`.

### Widget

- Replace static data with constructor params.
- Pure UI only.
- No direct Cubit/Bloc access.
- Callbacks via params.
- One class per file.

## 6. UI States

Fetch APIs:

- loading
- error
- empty
- success

Mutation APIs:

- submit loading
- success feedback
- error feedback
- optional navigation

Use project components: `FetchLoading`, `SubmitLoading`, `Skeletonizer`, `StatesScreen`, `StatesScreenList`, `StatesScreenGrid`, `DialogsManager`, `SnackBarsManager`, `BottomSheetsManager`.

## 7. Forms

If API is triggered by form, call `/add_form_flow`.
Rules:

- Controllers and `GlobalKey<FormState>` in Cubit/Bloc.
- Use `validateAndScroll()`.
- Call `HelperFunctions.unFocusKeyboard()`.
- Use project fields/buttons/validators.
- Use localized `StringsManager`.

## 8. Pagination

If paginated, call `/add_paginated_list`.
Use:

- `PaginatedResult<T>`
- `.toPaginatedResult()`
- `PaginationMixin<TState,TItem>`
- `initPagination()` in constructor
- `disposePagination()` in `close()`
- `fetchPage(int page)`
- `getItems({int page = 1, bool showLoading = true})`
- `StatesScreenList/Grid` with `cubit.paginationController`

## 9. Search / Filters

- Keep filters in Cubit/Bloc.
- Debounce search if utility exists.
- Reset pagination when filters change.
- Prefer API filtering over UI filtering for remote data.
- Use clear methods: `updateSearchQuery`, `applyFilters`, `clearFilters`.

## 10. Tests

Call `/generate_tests`.
Add/update:

- Model parsing
- Mapper conversion
- Repository behavior
- UseCase success/failure
- Cubit states: initial/loading/success/error/showLoading false
- Widget states: loading/error/empty/success/submit/form validation
  Use `.fake()`, `.fakeList()`, `bloc_test`, custom matchers, and `pumpApp`.

## 11. Review

Call `/review_pr`.
Verify:

- Endpoints in `ApiConstants`
- DataSource uses `ApiService`
- Interface + real + fake datasource
- Repository returns entities
- No DTOs in presentation
- Safe mappers
- Typed descriptive `StateStatus<T>`
- Screen/Section/Widget boundaries
- Design preserved
- States handled
- Tests updated
- No hardcoded strings/colors
- No unnecessary files

## Final Output

```md
## Completed Workflow(s)

1. ...

## Connected APIs

- METHOD /endpoint

## Updated Feature

...

## Files Changed

- ...

## State Management

- ...

## UI States Added

- Loading / Empty / Error / Success / Submit loading

## Tests

- ...

## Review Notes

- ...

## Remaining Assumptions

- ...
```
