---
trigger: model_decision
description: "Flutter Architecture Rule: 05_networking_and_data_layer.md"
---

# 05. Networking and Data Layer Standards

This document defines the usage of `ApiService` and mandatory data handling patterns.

---

## 1. Networking (`ApiService`)
Located in `core/network/api_service.dart`. **Always** use this service for HTTP requests.

| Function | When to Use | Typical Example |
| :--- | :--- | :--- |
| **`get<T>`** | Single object fetch. | `apiService.get<MyDto>(...)` |
| **`getList<T>`** | List of objects. | `apiService.getList<MyDto>(...)` |
| **`getObject<T>`** | Response inside `GeneralResponseModel`. | `apiService.getObject<MyDto>(...)` |
| **`post/put/delete`** | Mutations/Standard API calls. | `apiService.post<MyDto>(...)` |

### Automated UI Parameters:
- **`showLoading: true`**: Shows a global overlay spinner. Use for POST/PUT/DELETE mutations.
- **`showError: true`**: (Default) Shows error snackbar and logs to Crashlytics on failure.

---

## 2. Data Flow & Mappers
- **`ApiConstants`**: ALL endpoints must reside here. NO hardcoded strings in code.
- **Mappers**: Extensions in `data/mappers/` that convert DTO -> Domain Entity.
- **Naming**: Use `toModel()` for single objects and `toModelList()` for lists.
- **Return Types**: Repositories MUST return entities directly (e.g., `Future<MyEntity>`).

---

## 3. Real vs. Fake Data Sources (The Mirror Pattern)
To ensure testability and parallel development, every data source MUST follow the Double Implementation pattern across separate files:

| File Type | Purpose | Content / Logic |
| :--- | :--- | :--- |
| **Interface** | Definition | `abstract class MyDataSource` |
| **Real Impl** | Production | `MyDataSourceImpl` (uses `ApiService`) |
| **Fake Impl** | Mocking | `FakeMyDataSourceImpl` (uses `fakeFunction`) |

### Mandatory Rules:
- **Environment Switch**: Handle DI in the module via `ConstantsManager.isDebug`.
- **Pure Production**: NEVER include `if (isDebug)` or `fakeFunction` inside the real implementation.
- **Fake Logic**: Wrap static fake responses in `await fakeFunction(() => Model.fake())`.
- **Media**: All images in fake data MUST be high-quality, real descriptive images from the internet.
