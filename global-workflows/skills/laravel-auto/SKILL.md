---
name: laravel-auto
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Analyze the user request, detect the required Laravel task type, select the correct workflow or combination of workflows, and run them in a safe order while respecting the project Laravel rules.
---

# Laravel Auto Workflow Router

## Goal

Analyze the user request, detect the required Laravel task type, select the correct workflow or combination of workflows, and run them in a safe order while respecting the project Laravel rules.

This router is designed for a Laravel + Filament + HMVC/nWidart + Clean Architecture project.

## Core Principles

- Do not execute blindly.
- First classify the task.
- If the task requires code changes, always start with planning.
- If requirements are unclear, ask one concise clarification question before implementation.
- If multiple workflows are needed, call them in the safest order.
- Do not skip tests for implementation tasks.
- Do not skip API documentation and Postman updates for endpoint changes.
- Do not skip review after implementation.
- Always respect:
    - Clean Architecture
    - SOLID
    - TDD
    - Thin Controllers
    - Form Requests for validation
    - API Resources for responses
    - Unified API response structure
    - Services for business logic
    - Repositories for Eloquent/DB queries
    - Policies/Gates for authorization
    - Modules under `Modules/`
    - Filament resources inside modules
    - Arabic/English translation standards
    - Pest testing standards
    - API documentation and Postman sync

## Available Workflows

Use only these workflow names unless the user explicitly adds more:

- `/create_module`
- `/add_api_endpoint`
- `/generate_tests`
- `/review_pr`
- `/fix_bug`
- `/create_model_table`
- `/add_filament_resource`
- `/add_translation`
- `/security_check`
- `/optimize_queries`
- `/add_policy_authorization`
- `/add_job_event_listener`
- `/update_api_docs`
- `/cleanup`
- `/commit_message`

## Initial Classification

Before calling any workflow, output:

```md
## Detected Task Type

...

## Selected Workflow(s)

1. ...

## Reason

...

## Approval Needed

Yes / No
```

## Approval Rules

### Approval is required when:

- Creating files.
- Modifying files.
- Running migrations.
- Changing database schema.
- Adding endpoints.
- Changing API response shape.
- Adding or changing authorization.
- Updating Filament resources.
- Adding jobs, events, or listeners.
- Refactoring or cleanup.
- Updating documentation files.

### Approval is not required when:

- Reviewing code.
- Generating a commit message.
- Explaining architecture.
- Reading or inspecting files.
- Producing a plan only.

If approval is required, stop after the plan and wait for explicit approval before implementation.

## Single-Workflow Routing

### New Laravel module

If the request is about creating a new module, domain, bounded context, or major feature area:

Call:

1. `/create_module`

Examples:

- "Create Orders module"
- "Add a new Doctors module"
- "Build a module for appointments"

---

### API endpoint

If the request is about adding, updating, or fixing an endpoint, route, controller method, request validation, resource response, or API behavior:

Call:

1. `/add_api_endpoint`

Examples:

- "Add products list endpoint"
- "Create POST /appointments"
- "Update patient profile API"

---

### Tests only

If the request is only about tests:

Call:

1. `/generate_tests`

Examples:

- "Write tests for OrderService"
- "Add Pest tests for login endpoint"
- "Generate endpoint tests"

---

### PR or diff review

If the request is about reviewing current changes, PR readiness, current diff, or code quality review:

Call:

1. `/review_pr`

Examples:

- "Review my changes"
- "Check this PR"
- "Is this ready to merge?"

---

### Bug fix

If the request describes broken behavior, failing tests, wrong API response, exception, or incorrect business logic:

Call:

1. `/fix_bug`

Examples:

- "Fix 500 error in products endpoint"
- "Validation returns wrong message"
- "Filament action does not update status"

---

### Database model/table

If the request is about a new table, migration, model, factory, seeder, casts, relationships, or indexes:

Call:

1. `/create_model_table`

Examples:

- "Create categories table"
- "Add relation between doctors and specialties"
- "Create migration and model for coupons"

---

### Filament admin

If the request is about Filament Resource, custom page, widgets, table actions, relation managers, forms, tables, dashboard, navigation, or admin UI:

Call:

1. `/add_filament_resource`

Examples:

- "Add Filament CRUD for products"
- "Create dashboard stats widget"
- "Add approve action in Filament"

---

### Translation / localization

If the request is about Arabic/English, `Accept-Language`, translatable fields, localized API responses, validation messages, Filament labels, or RTL inputs:

Call:

1. `/add_translation`

Examples:

- "Make product name translatable"
- "Return localized category name"
- "Add Arabic labels in Filament"

---

### Security review

If the request asks for security review or touches sensitive areas such as auth, passwords, roles, permissions, public endpoints, file uploads, raw SQL, or sensitive logs:

Call:

1. `/security_check`

Examples:

- "Review endpoint security"
- "Check if this upload flow is safe"
- "Audit auth logic"

---

### Query performance

If the request mentions slow endpoint, N+1, indexes, eager loading, large datasets, pagination performance, or query optimization:

Call:

1. `/optimize_queries`

Examples:

- "Optimize products list"
- "Fix N+1 in orders endpoint"
- "Make dashboard query faster"

---

### Authorization

If the request is specifically about permissions, policies, gates, roles, or access control:

Call:

1. `/add_policy_authorization`

Examples:

- "Only admins can delete users"
- "Add policy for appointments"
- "Prevent users from editing others' orders"

---

### Jobs / Events / Listeners

If the request is about emails, SMS, notifications, external APIs, background processing, queued tasks, events, listeners, or long-running side effects:

Call:

1. `/add_job_event_listener`

Examples:

- "Send email after order is placed"
- "Queue SMS notification"
- "Call external payment API after checkout"

---

### API docs / Postman

If the request is only about API documentation or Postman collection:

Call:

1. `/update_api_docs`

Examples:

- "Update Postman collection"
- "Document the auth endpoints"
- "Sync API docs with current routes"

---

### Cleanup

If the request is about low-risk cleanup, imports, types, formatting, removing debug statements, replacing env usage, or minor refactoring:

Call:

1. `/cleanup`

Examples:

- "Clean this service"
- "Remove unused imports"
- "Fix code style issues"

---

### Commit message

If the request is about generating a commit message:

Call:

1. `/commit_message`

Examples:

- "Write commit message"
- "Generate commit from current diff"

## Multi-Workflow Routing

Use multiple workflows when a task naturally requires more than one area.

### New API endpoint

For any new endpoint or endpoint update that changes behavior:

Call in this order:

1. `/add_api_endpoint`
2. `/generate_tests`
3. `/update_api_docs`
4. `/review_pr`

Reason:

- Endpoint implementation needs validation, service/repository/resource work.
- Tests are mandatory.
- API docs and Postman must remain synced.
- Review catches architecture, security, performance, and documentation issues.

---

### New module with API

For a new module that includes API functionality:

Call in this order:

1. `/create_module`
2. `/create_model_table`
3. `/add_api_endpoint`
4. `/generate_tests`
5. `/update_api_docs`
6. `/review_pr`

---

### New module with API and Filament admin

For a complete module with database, API, and dashboard CRUD:

Call in this order:

1. `/create_module`
2. `/create_model_table`
3. `/add_api_endpoint`
4. `/add_filament_resource`
5. `/generate_tests`
6. `/update_api_docs`
7. `/review_pr`

---

### Filament CRUD for an existing model

For admin CRUD when the model/table already exists:

Call in this order:

1. `/add_filament_resource`
2. `/generate_tests`
3. `/review_pr`

---

### Filament CRUD for a new model

For admin CRUD when the model/table does not exist yet:

Call in this order:

1. `/create_model_table`
2. `/add_filament_resource`
3. `/generate_tests`
4. `/review_pr`

---

### Bug in existing endpoint

For bugs that affect an API endpoint:

Call in this order:

1. `/fix_bug`
2. `/generate_tests`
3. `/update_api_docs` only if API behavior, request, response, or status codes changed
4. `/review_pr`

---

### Bug in Filament

For bugs in Filament resources, pages, widgets, actions, or relation managers:

Call in this order:

1. `/fix_bug`
2. `/add_filament_resource` only if Filament structure or behavior needs modification
3. `/generate_tests`
4. `/review_pr`

---

### Add translatable model field

For a new or updated translatable attribute:

Call in this order:

1. `/add_translation`
2. `/create_model_table` if database changes are required
3. `/add_api_endpoint` if API output/input changes
4. `/add_filament_resource` if admin UI changes
5. `/generate_tests`
6. `/update_api_docs` if API behavior changed
7. `/review_pr`

---

### Add authorization to endpoint or admin action

For permissions, roles, policies, and access control:

Call in this order:

1. `/add_policy_authorization`
2. `/generate_tests`
3. `/update_api_docs` if endpoint behavior or error response changed
4. `/review_pr`

---

### Security-sensitive implementation

For changes involving auth, permissions, passwords, uploads, public endpoints, external API, or sensitive data:

Call in this order:

1. `/security_check`
2. The matching implementation workflow:
    - `/add_api_endpoint`
    - `/add_filament_resource`
    - `/add_policy_authorization`
    - `/add_job_event_listener`
    - `/fix_bug`
3. `/generate_tests`
4. `/update_api_docs` if API behavior changed
5. `/review_pr`

---

### Performance optimization

For slow queries, N+1, indexing, or large datasets:

Call in this order:

1. `/optimize_queries`
2. `/generate_tests`
3. `/review_pr`

If database indexes or schema changes are needed, include:

1. `/create_model_table`

Correct order:

1. `/optimize_queries`
2. `/create_model_table` if migration/index change is required
3. `/generate_tests`
4. `/review_pr`

---

### Side effect after business action

For emails, SMS, notifications, webhooks, external calls, background work:

Call in this order:

1. `/add_job_event_listener`
2. `/generate_tests`
3. `/update_api_docs` if endpoint behavior changed
4. `/review_pr`

---

### Cleanup with tests

For cleanup that may touch behavior or architecture:

Call in this order:

1. `/cleanup`
2. `/generate_tests` if behavior or tested code changed
3. `/review_pr`

---

### Prepare PR

If the user asks to prepare a PR after implementation:

Call in this order:

1. `/generate_tests`
2. `/update_api_docs` if endpoint changes exist
3. `/review_pr`
4. `/commit_message`

## Conflict Resolution

### If two workflows overlap:

Choose the more specific workflow first.

Examples:

- Filament translation issue → `/add_translation`, then `/add_filament_resource`
- API authorization issue → `/add_policy_authorization`, then `/add_api_endpoint`
- Endpoint performance issue → `/optimize_queries`, then `/generate_tests`

### If the task is ambiguous:

Ask one concise clarification question.

Examples:

- "Is this endpoint for public users or authenticated users?"
- "Is this model inside an existing module or should I create a new module?"
- "Should this data be shown in the API, Filament, or both?"

### If the user asks for a quick implementation that violates rules:

Do not comply blindly. Explain the risk and propose the Laravel-standard alternative.

## Final Output After Running Workflows

After the selected workflows complete, summarize:

```md
## Completed Workflow(s)

1. ...

## What Changed

- ...

## Tests

- ...

## Documentation

- ...

## Review Notes

- ...

## Remaining Risks / Assumptions

- ...
```
