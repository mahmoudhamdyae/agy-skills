---
name: add-filament-resource
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Create or update a Filament Resource inside a module while following bilingual, modular, authorization, and UX standards.
---

# Add Filament Resource

## Goal

Create or update a Filament Resource inside a module while following bilingual, modular, authorization, and UX standards.

## Mandatory Rules

- Filament resources must live inside the module.
- Labels must use translations with module-namespaced keys.
- Do not hardcode Arabic or English labels.
- Bilingual fields must be separated clearly, preferably using Tabs or Sections.
- Arabic inputs must use `->dir('rtl')`.
- Destructive actions must require confirmation.
- Use Heroicons v2.
- Register resources through the module plugin or panel configuration according to the project pattern.
- Follow Plan → Implement → Review.

## Workflow

### 1. Plan

1. Identify the target module and model.
2. Inspect existing Filament resources.
3. Identify:
    - Form fields
    - Table columns
    - Filters
    - Actions
    - Bulk actions
    - Relation managers
    - Navigation group
    - Navigation sort
    - Translations
    - Authorization needs
4. Determine whether fields are translatable.
5. Propose the Filament structure and wait for approval.

### 2. Implement

After approval only:

1. Create or update the Resource inside:
   `Modules/{Module}/app/Filament/Resources`
2. Add form schema.
3. For translatable fields:
    - Use `name.en`
    - Use `name.ar`
    - Use Tabs or Sections.
    - Apply `->dir('rtl')` to Arabic fields.
4. Add table columns.
5. Add filters.
6. Add actions and bulk actions.
7. Add confirmation for destructive actions.
8. Add notifications using Filament Notification.
9. Add translation keys in Arabic and English files.
10. Register the resource if needed.
11. Add tests where project conventions support it.

### 3. Review

1. Verify labels use `__()`.
2. Verify navigation labels are translated.
3. Verify Arabic fields are RTL.
4. Verify destructive actions require confirmation.
5. Verify resource location is module-scoped.
6. Summarize:
    - Resource added/updated
    - Fields
    - Columns
    - Filters
    - Actions
    - Translation keys
