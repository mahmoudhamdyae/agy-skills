---
name: laravel-commit-message
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Generate a clean commit message from the current staged or unstaged diff.
---

# Commit Message

## Goal

Generate a clean commit message from the current staged or unstaged diff.

## Mandatory Rules

- Do not modify files.
- Use imperative mood.
- Keep the message concise and descriptive.
- Match the actual diff.
- Do not claim tests passed unless verified.

## Workflow

### 1. Inspect

1. Read the current diff.
2. Identify the main purpose of the change.
3. Determine the commit type:
    - feature
    - fix
    - refactor
    - test
    - docs
    - chore
    - security
    - performance

### 2. Generate

Create one recommended commit message using this style:

````text
Add post creation endpoint with validation

For complex changes, include an optional body:

Add post creation endpoint with validation

- Add Form Request and API Resource
- Move business logic into Service
- Add Pest feature tests
- Update API documentation and Postman collection

3. Validate

Ensure the message:

Is imperative.
Is concise.
Explains intent.
Does not list every file.
Matches the actual changes.
Output Format
## Recommended Commit Message

```text
...
Why
...
````
