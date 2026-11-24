---
trigger: model_decision
description: "Flutter Architecture Rule: 02_architecture_clean.md"
---

# 02. Clean Architecture Standards

This document defines the architectural layers, their responsibilities, and the mandatory data flow.

---

## 1. Directory Structure

| Layer | Responsibility | Mandatory Content |
| :--- | :--- | :--- |
| **`presentation/`** | UI & State Management | Screens, Sections, Widgets, Blocs/Cubits. **NO logic/API here.** |
| **`domain/`** | Pure Business Logic | **Entities** (with `fake()`), **Usecases**, **Repository Interfaces**. |
| **`data/`** | Data Source & Processing | **Data Sources** (Double Impl), **Repositories**, **Models/DTOs** (with `fake()`), **Mappers**. |
| **`core/`** | Shared Foundation | Networking, DI, Themes, Extensions, Managers, Base classes. |

### The Layer Rules:
- **Dependency Flow**: Every feature MUST depend on `core`.
- **Isolation**: Domain layer has ZERO dependencies on other layers (except `core`).
- **Feature Structure**: Every feature follows: `lib/features/<name>/[data, domain, presentation]`.

---

## 2. Data Flow (The logic path)
1. **UI**: Triggers an Event.
2. **Bloc/Cubit**: Calls a **Usecase**.
3. **Usecase**: Returns `Future<T>` from a **Repository interface** (No `Either` or `dartz`).
4. **Data Repo**: Fetches from **DataSource** via `ApiService`.
5. **Data Repo**: Maps DTO -> Entity and returns it.
6. **Bloc/Cubit**: Catches `ServerException`, emits `.error()` or `.success()`.
7. **UI**: Updates based on State.

---

## 3. Implementation Patterns

### Double Implementation (Data Sources)
To ensure testability during backend unavailability, every data source MUST implement:
1. **Interface**: `abstract class MyDataSource`.
2. **Real Impl**: `MyDataSourceImpl` (uses `ApiService`).
3. **Fake Impl**: `FakeMyDataSourceImpl` (uses `fakeFunction`).

### Model & Entity Fakes
- Every Model and Entity MUST include `static fake()` and `static fakeList()`.
- Fake data MUST use real, descriptive images from the internet (e.g., Unsplash).

---

## 4. SOLID & Quality
- **Dependency Inversion**: High-level modules depend on abstractions (interfaces).
- **Single Responsibility**: Each class/file has exactly one reason to change.
- **Maintenance**: Respect existing patterns; preserve style and naming during modifications.
- **Testing**: Prioritize behavior-based unit tests for the domain layer.
