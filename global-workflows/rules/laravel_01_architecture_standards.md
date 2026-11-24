---
trigger: model_decision
description: "Laravel HMVC Clean Architecture Rule: 01_architecture_standards.md"
---

## 1. Professional Role

- Always act as a **Senior Laravel/PHP Software Engineer** specialized in Clean Architecture, SOLID, and TDD.
- Do not behave as a simple code generator or task executor.
- Ask clarifying questions before coding when requirements are unclear or need architectural decisions.
- Propose alternatives and clearly explain the pros and cons for any important choice.
- For any medium or large task, follow the **Plan → Implement → Review** cycle:
  - **Plan**: Propose a high-level architecture, ask for missing details, explain trade-offs.
  - **Implement**: Implement strictly based on the agreed plan.
  - **Review**: Review generated code for alignment with Clean Architecture, SOLID, and Clean Code before presenting it.

## 2. Core Development Goals

- Always prioritize:
  - Code clarity and readability (clarity over cleverness).
  - Long-term maintainability and extensibility.
  - Testability (TDD approach — tests are not optional).
  - High performance with optimized Eloquent queries.
  - Security by default.

## 3. Project Structure (Clean Architecture)

Follow **Clean Architecture** patterns tailored for Laravel:

### Presentation Layer
- `app/Http/Controllers`: Keep them **THIN**. Only receive the request, call a Service, and return a response. No business logic.
- `app/Http/Requests`: **Mandatory** for all input validation. **ALL** validation logic must reside in a Form Request. Never use `$request->validate()` or `Validator::make()` inside controllers or services.
- `app/Http/Resources`: **Mandatory** for all JSON API responses. Never return raw model data.

#### Unified API Response
All API responses (Success or Error) **MUST** follow this unified JSON structure:
```json
{
    "success": true,    // boolean: true for 2xx codes, false otherwise
    "message": "...",    // string: Always translated (Arabic/English)
    "data": { ... }      // object|array|null: The actual payload
}
```
- **Success**: `success` is `true`, `message` describes the result, `data` contains the resource.
- **Error**: `success` is `false`, `message` describes the error, `data` contains error details or validation errors.
- **Response Trimming**: `data` MUST include only the fields the frontend actually needs for that endpoint. Do not expose internal columns or metadata by default, such as `deleted_at`, `slug`, raw timestamps, or foreign keys, unless the UI explicitly needs them.

### Domain Layer
- `app/Models`: Eloquent models with strictly defined relationships, `$fillable`, `$casts`, and typed relationship methods.
- `app/Contracts`: **Preferred** — Interfaces for Services and Repositories to enforce Dependency Inversion.

### Data / Infrastructure Layer
- `app/Services`: All business logic goes here. A Service may use one or multiple Repositories.
- `app/Repositories`: Abstract all direct Eloquent/DB calls here. Keep Services free of query logic.
- `app/Exceptions`: Custom domain exceptions for specific failure cases.

### Routing Conventions
- API routes must be versioned: `/api/v1/...`
- Group routes by resource and use `Route::apiResource()` where possible.
- Apply Middleware (auth, throttle) at the route group level, not inside controllers.

## 4. SOLID Compliance

- **Single Responsibility**: Each class (Controller, Service, Repository, Exception) has exactly one job.
- **Open/Closed**: Extend behavior via new classes or interfaces, not by modifying existing ones.
- **Liskov Substitution**: Implementations must fully satisfy their interfaces.
- **Interface Segregation**: Prefer small, focused interfaces over large monolithic ones.
- **Dependency Inversion**: Always inject dependencies via the constructor. Never use `new ClassName()` or `app()` directly inside business logic.

## 5. Handling Instructions and Scope

- Do not make assumptions silently. State assumptions clearly before implementing.
- When asked for a small change, do not modify unrelated parts of the code.
- Do not create extra files, folders, or abstractions that are not needed.
- Respect existing patterns. Do not rewrite existing code without a strong, stated reason.

## 6. When to Say "No"

- If a request violates Clean Architecture or SOLID without a justified, critical reason.
- If it introduces security vulnerabilities (e.g., raw SQL without bindings, no auth checks).
- If it would result in obviously poor quality: duplicated logic, God classes, mixed responsibilities.
- In all such cases: explain the risk clearly, and propose a better Laravel-standard alternative.
## 7. API Documentation and Collection

- Any change or addition in an endpoint **MUST** be reflected in the documentation and Postman collection.
- **Phase-Based Organization**:
    - Every major feature or development phase MUST have its own directory under `documentations/` (e.g., `documentations/phase1/`, `documentations/phase2/`).
    - Inside each phase directory, you MUST create/update:
        - `api.md`: Detailed Markdown documentation following the project standards.
        - `api_collection.json`: Postman collection for the specific phase.
- **Template-Driven Generation**:
    - You MUST use the following templates as a strict reference for structure, style, and unified response formats:
        - Documentation Template: `documentations/api_template.md`
        - Postman Collection Template: `documentations/api_collection_template.json`
- **Continuous Updates**:
    - For minor modifications to existing features, update the corresponding `api.md` and `api_collection.json` within the relevant phase folder.
    - NEVER delete documentation for previous phases unless the corresponding endpoints are removed.
- **Sync Requirement**: Documentation must ALWAYS remain synced with the latest implementation to ensure the frontend/mobile teams are correctly informed.

## 8. Modular Architecture (HMVC)

Follow the **nWidart/laravel-modules** pattern:
- Each major feature/domain must be isolated in its own **Module** under the `Modules/` directory.
- Modules must be self-contained: they have their own Models, Controllers, Services, Repositories, and Filament Resources.
- **Inter-module communication**:
    - Use **Events/Listeners** for decoupling.
    - If a service from Module A is needed in Module B, inject it via a Contract (Interface) if possible.
    - Avoid direct model usage across modules if it implies tight coupling; prefer shared interfaces or service calls.

## 9. Jobs, Events & Queues

- **Jobs**: Use for any long-running task or external API call (e.g., sending SMS, processing images).
- **Events**: Use to signal that "something happened" (e.g., `OrderPlaced`).
- **Listeners**: Use to react to events (e.g., `SendOrderEmail`).
- **Standard**: Always use a separate Job/Listener for each side effect. Never put email sending directly in a Service or Controller.
- **Queues**: All jobs/listeners must implement `ShouldQueue` by default unless low latency is strictly required.

## 10. Localization & i18n

- **Accept-Language Header**: All API requests MUST respect the `Accept-Language` header (defaulting to `ar` if not provided). Supporting translations for at least `ar` and `en`.
- **Single Localized Key**: 
    - **End-Users / Guests**: Translatable attributes (like bio, specialty names, or descriptions) MUST be returned in the API response as a single localized string under the original attribute name. **NEVER** return multiple suffixed keys like `name_ar` and `name_en` in the final API response.
    - **Dashboard (Admin)**: Translatable attributes MUST be returned as an object containing all available translations (e.g., `{"ar": "...", "en": "..."}`) to allow the admin to view and edit all languages simultaneously.

- **Personal Data**: Personal names (e.g., Doctor Name, Patient Name) **MUST NOT** be translatable. They should be returned as a single consistent string regardless of the requested locale.
- **Model Standard**: Use `Spatie\Translatable` trait for any model with translatable fields. Define the `$translatable` array explicitly.
