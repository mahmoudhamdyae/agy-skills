---
name: write-docs
description: >-
  Flutter Clean Architecture & S-S-W workflow: Create or update concise developer documentation for a feature, module, workflow, or architecture decision.
---

# Write Docs

## Goal

Create or update concise developer documentation for a feature, module, workflow, or architecture decision.

## Mandatory Rules

- Documentation must reflect the actual codebase.
- Do not invent behavior or architecture.
- Keep documentation concise and practical.
- Mention assumptions explicitly.
- Do not modify code unless explicitly asked.
- Prefer examples from existing project patterns.

## Workflow

### 1. Plan

1. Inspect the relevant files.
2. Identify the target audience:
   - Future developer
   - Reviewer
   - QA
   - Backend team
   - Product/PM
3. Identify the correct documentation location:
   - Feature README
   - Architecture doc
   - Inline doc comments
   - PR description
   - Setup guide
4. Propose the documentation structure and wait for approval if files will be changed.

### 2. Implement

After approval only, write documentation covering:

1. Purpose.
2. Architecture overview.
3. Data flow.
4. State management flow.
5. Important files.
6. How to use or extend the feature.
7. Testing strategy.
8. Known limitations or assumptions.

### 3. Review

1. Verify docs match actual implementation.
2. Remove vague or outdated statements.
3. Keep language clear and technical.
4. Summarize:
   - Docs added/updated
   - Main topics covered
   - Any missing context
