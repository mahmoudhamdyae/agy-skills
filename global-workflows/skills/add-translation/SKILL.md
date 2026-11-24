---
name: add-translation
description: >-
  Laravel + Filament + HMVC Clean Architecture workflow: Add or update Arabic and English translation support for API, Filament, validation, notifications, or translatable model fields.
---

# Add Translation Support

## Goal

Add or update Arabic and English translation support for API, Filament, validation, notifications, or translatable model fields.

## Mandatory Rules

- API requests must respect the `Accept-Language` header.
- Default locale is Arabic when not provided.
- End-user API responses must return one localized value under the original attribute name.
- Never return `name_ar` and `name_en` to end-users.
- Admin/dashboard responses may expose all translations as an object.
- Personal names must not be translatable.
- Use Spatie Translatable for translatable model fields when available.
- Translation files must exist for both `ar` and `en`.
- Filament labels must use module-namespaced translation keys.
- Arabic Filament inputs must use `->dir('rtl')`.

## Workflow

### 1. Plan

1. Identify the translation scope:
    - API message
    - Validation message
    - Filament label
    - Notification
    - Model attribute
    - Resource output
2. Determine whether the field should be translatable.
3. Verify personal data is not translated.
4. Identify the correct module translation files:
    - `Modules/{Module}/lang/ar/...`
    - `Modules/{Module}/lang/en/...`
5. Propose changes and wait for approval.

### 2. Implement

After approval only:

1. Add or update Arabic translation keys.
2. Add or update English translation keys.
3. Use `__()` with module-namespaced keys.
4. For translatable model fields:
    - Use JSON columns.
    - Use Spatie Translatable if available.
    - Define `$translatable` explicitly.
5. Update API Resources to return localized single values for end-users.
6. Update Filament forms to expose both languages.
7. Apply RTL direction to Arabic fields.
8. Add tests for localized API responses where applicable.

### 3. Review

1. Verify Arabic response.
2. Verify English response.
3. Verify Filament labels.
4. Verify validation messages.
5. Verify no `name_ar` / `name_en` leaks in end-user API responses.
6. Summarize:
    - Keys added
    - Files changed
    - API behavior
    - Admin behavior
