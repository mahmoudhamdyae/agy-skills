---
name: update-api-docs
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Create or update Markdown API documentation and Postman collection for endpoint changes.
---

# Update API Documentation

## Goal

Create or update Markdown API documentation and Postman collection for endpoint changes.

## Mandatory Rules

- Any endpoint change must update documentation.
- Any endpoint change must update Postman collection.
- Use:
    - `documentations/api_template.md`
    - `documentations/api_collection_template.json`
- Organize docs by phase:
    - `documentations/phase1/`
    - `documentations/phase2/`
    - etc.
- Do not delete previous phase documentation unless endpoints were removed.
- Documentation must match actual implementation.
- Unified response format must be documented.

## Workflow

### 1. Plan

1. Identify changed endpoints.
2. Identify relevant phase folder.
3. Inspect existing docs and collection.
4. Compare actual implementation with docs.
5. Identify missing or stale documentation.
6. Propose documentation updates and wait for approval if files will change.

### 2. Implement

After approval only:

1. Update `api.md`.
2. Include:
    - Endpoint name
    - Method
    - URL
    - Auth requirements
    - Headers
    - Request body
    - Validation rules
    - Success response
    - Error responses
    - Notes
3. Update `api_collection.json`.
4. Ensure sample responses use:
    - `success`
    - `message`
    - `data`
5. Ensure messages and examples match localized behavior where needed.

### 3. Review

1. Verify docs match routes.
2. Verify docs match Resources.
3. Verify Postman collection is valid JSON.
4. Summarize:
    - Endpoints documented
    - Collection updated
    - Phase folder
