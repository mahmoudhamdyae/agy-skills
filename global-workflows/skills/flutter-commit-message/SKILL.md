---
name: flutter-commit-message
description: >-
  Flutter Clean Architecture & S-S-W workflow: Generate a clean commit message from the current staged or unstaged diff.
---

# Commit Message

## Goal

Generate a clean commit message from the current staged or unstaged diff.

## Mandatory Rules

- Do not modify files.
- Follow the project's commit convention.
- Use imperative, concise wording.
- Prefer Conventional Commits format.
- Summarize intent, not every changed file.
- Mention tests only when relevant.

## Workflow

### 1. Inspect

1. Read the current diff.
2. Identify the main purpose of the change.
3. Determine the commit type:
   - `feat`
   - `fix`
   - `refactor`
   - `test`
   - `docs`
   - `style`
   - `chore`
   - `perf`
   - `build`
   - `ci`

### 2. Generate

Create one recommended commit message:

````text
type: imperative summary

For complex changes, include a body:
type(scope): imperative summary

- Explain key architectural change
- Mention testing impact
- Mention migration or side effects if any

3. Validate

Ensure the message:

Is concise.
Uses imperative mood.
Does not over-describe file changes.
Matches the actual diff.
Does not claim tests were run unless verified.
Output Format
## Recommended Commit Message

```text
...
Why
...
````
