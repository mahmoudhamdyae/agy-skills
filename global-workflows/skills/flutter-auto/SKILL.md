---
name: flutter-auto
description: >-
  Flutter Clean Architecture & S-S-W workflow: Analyze the user request, detect the Flutter task type, select the correct workflow(s), and run them safely while respecting project Flutter rules.
---

# Flutter Auto Workflow Router

## Goal

Analyze the user request, detect the Flutter task type, select the correct workflow(s), and run them safely while respecting project Flutter rules.

Designed for Flutter with Clean Architecture, S-S-W, Bloc/Cubit, `StateStatus<T>`, Core Foundation, pagination, animations, strict tests, Figma-to-Flutter, image-to-Flutter, and API-to-design workflows.

## Core Principles

- Do not execute blindly.
- Classify first.
- If code changes are needed, start with planning.
- Ask one concise question only when requirements are unsafe/unclear.
- If multiple workflows are needed, call them in the safest order.
- Do not skip tests or final review.
- Preserve existing design unless implementing from Figma or uploaded images.
- If a Figma link exists, prefer `/figma_to_screens` over generic `/create_feature`.
- If uploaded images/screenshots are provided for UI implementation, prefer `/images_to_flutter_design`.
- If API specs target an existing design, prefer `/connect_design_to_apis` over generic `/api_endpoint`.
- If Figma/images + APIs are both provided, build UI first, then connect APIs.
- Always respect:
  - Plan → Implement → Review
  - Clean Architecture / SOLID
  - Core Foundation First
  - Screen-Section-Widget
  - Bloc/Cubit + typed descriptive `StateStatus<T>`
  - DataSource double implementation
  - `.fake()` / `.fakeList()`
  - project widgets/extensions
  - responsive styling
  - pagination/animation standards
  - Unit, Bloc, Widget, and Golden tests where applicable

## Available Workflows

Use only these unless user adds more:

- `/generate_tests`
- `/review_pr`
- `/fix_bug`
- `/refactor_safely`
- `/write_docs`
- `/security_check`
- `/api_endpoint`
- `/commit_message`
- `/migration_check`
- `/cleanup`
- `/create_feature`
- `/add_paginated_list`
- `/add_animated_ui`
- `/add_form_flow`
- `/figma_to_screens`
- `/images_to_flutter_design`
- `/connect_design_to_apis`

## Initial Output

Before calling workflows:

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

Approval required for:

- creating/modifying files
- adding feature/API/state/UI behavior
- implementing Figma screens
- implementing UI from uploaded images/screenshots
- exporting/copying Figma assets
- connecting APIs to a design
- refactor/cleanup/tests/docs
- pagination/animations/forms

No approval required for:

- review
- commit message
- explanation
- inspection
- plan/classification only

If approval is required, stop after plan and wait.

## Design/API Detection

### Figma work

Detect when request includes:

- Figma URL, `figma.com`, "Figma", "design link", "convert design", "implement design/screens"
- Arabic: "لينك فيجما", "ديزاين فيجما", "اعمل من لينك فيجما"

Use:

1. `/figma_to_screens`

### Uploaded image to Flutter design

Detect when request includes uploaded image(s), screenshots, UI mockups, or phrases:

- "convert uploaded images"
- "image to Flutter"
- "screenshot to Flutter"
- "UI mockup to code"
- Arabic: "حول الصور", "الصور المرفوعة", "من الصورة لكود", "صورة لكود ديزاين", "سكرين شوت لكود"

Use:

1. `/images_to_flutter_design`

### API-to-existing-design

Detect when request includes:

- API specs, endpoint list, Swagger/OpenAPI, Postman, request/response examples
- "connect APIs", "use these APIs"
- Arabic: "اربط التصميم بال APIs", "اربط الديزاين", "اربط الشاشة بال API"

Use:

1. `/connect_design_to_apis`

### Combined design + APIs

If Figma + APIs:

1. `/figma_to_screens`
2. `/connect_design_to_apis`
3. `/generate_tests`
4. `/review_pr`

If uploaded images + APIs:

1. `/images_to_flutter_design`
2. `/connect_design_to_apis`
3. `/generate_tests`
4. `/review_pr`

If Figma + uploaded images:

- Prefer `/figma_to_screens` as source of truth.
- Use uploaded images as secondary visual references only.

## Single-Workflow Routing

### Figma to Flutter screens

If implementing screen(s) from Figma:

1. `/figma_to_screens`

### Uploaded images to Flutter UI

If implementing screen(s) from uploaded images/screenshots/mockups:

1. `/images_to_flutter_design`

Examples:

- "حول الصور المرفوعة لكود Flutter"
- "Convert these screenshots to Flutter UI"
- "اعمل ديزاين من الصورة"

### Connect existing design to APIs

If existing UI/design should use provided APIs:

1. `/connect_design_to_apis`

### New Flutter feature

If creating a feature/screen flow without Figma or images:

1. `/create_feature`

### API integration

If backend integration is requested without explicit existing-design wording:

1. `/api_endpoint`

### Tests only

1. `/generate_tests`

### PR/diff review

1. `/review_pr`

### Bug fix

1. `/fix_bug`

### Safe refactor

1. `/refactor_safely`

### Documentation

1. `/write_docs`

### Security review

1. `/security_check`

### Commit message

1. `/commit_message`

### Response migration

For backend response shape, DTO/model fields, nullable fields, enum, pagination response:

1. `/migration_check`

### Cleanup

1. `/cleanup`

### Paginated list

For infinite scroll/list/grid pagination:

1. `/add_paginated_list`

### Animated UI

For entrance/staggered motion:

1. `/add_animated_ui`

### Form flow

For form/validation/controllers/submit:

1. `/add_form_flow`

## Multi-Workflow Routing

### Figma-only implementation

1. `/figma_to_screens`
2. `/generate_tests`
3. `/review_pr`

### Image-only implementation

1. `/images_to_flutter_design`
2. `/generate_tests`
3. `/review_pr`

### Figma with forms

1. `/figma_to_screens`
2. `/add_form_flow`
3. `/generate_tests`
4. `/review_pr`

### Images with forms

1. `/images_to_flutter_design`
2. `/add_form_flow`
3. `/generate_tests`
4. `/review_pr`

### Figma with paginated list

1. `/figma_to_screens`
2. `/add_paginated_list`
3. `/generate_tests`
4. `/review_pr`

### Images with paginated list

1. `/images_to_flutter_design`
2. `/add_paginated_list`
3. `/generate_tests`
4. `/review_pr`

### Figma with animations

1. `/figma_to_screens`
2. `/add_animated_ui`
3. `/generate_tests`
4. `/review_pr`

### Images with animations

1. `/images_to_flutter_design`
2. `/add_animated_ui`
3. `/generate_tests`
4. `/review_pr`

### Existing design + APIs

1. `/connect_design_to_apis`
2. `/generate_tests`
3. `/review_pr`

### Existing design + paginated API

1. `/connect_design_to_apis`
2. `/add_paginated_list`
3. `/generate_tests`
4. `/review_pr`

### Existing design + form submit API

1. `/connect_design_to_apis`
2. `/add_form_flow`
3. `/generate_tests`
4. `/review_pr`

### Figma + APIs

1. `/figma_to_screens`
2. `/connect_design_to_apis`
3. `/generate_tests`
4. `/review_pr`

If form:

1. `/figma_to_screens`
2. `/add_form_flow`
3. `/connect_design_to_apis`
4. `/generate_tests`
5. `/review_pr`

If pagination:

1. `/figma_to_screens`
2. `/connect_design_to_apis`
3. `/add_paginated_list`
4. `/generate_tests`
5. `/review_pr`

### Images + APIs

1. `/images_to_flutter_design`
2. `/connect_design_to_apis`
3. `/generate_tests`
4. `/review_pr`

If form:

1. `/images_to_flutter_design`
2. `/add_form_flow`
3. `/connect_design_to_apis`
4. `/generate_tests`
5. `/review_pr`

If pagination:

1. `/images_to_flutter_design`
2. `/connect_design_to_apis`
3. `/add_paginated_list`
4. `/generate_tests`
5. `/review_pr`

If form + pagination:

1. `/images_to_flutter_design`
2. `/add_form_flow`
3. `/connect_design_to_apis`
4. `/add_paginated_list`
5. `/generate_tests`
6. `/review_pr`

### New feature with API and UI, no Figma/images

1. `/create_feature`
2. `/api_endpoint`
3. `/generate_tests`
4. `/review_pr`

### New feature with form and API, no Figma/images

1. `/create_feature`
2. `/add_form_flow`
3. `/api_endpoint`
4. `/generate_tests`
5. `/review_pr`

### API endpoint only

1. `/api_endpoint`
2. `/generate_tests`
3. `/review_pr`

### Paginated API list, no Figma/image/design context

1. `/api_endpoint`
2. `/add_paginated_list`
3. `/generate_tests`
4. `/review_pr`

If feature missing:

1. `/create_feature`
2. `/api_endpoint`
3. `/add_paginated_list`
4. `/generate_tests`
5. `/review_pr`

### Animated screen/section, no Figma/images

1. `/create_feature` if missing
2. `/add_animated_ui`
3. `/generate_tests`
4. `/review_pr`

### Form with animations, no Figma/images

1. `/add_form_flow`
2. `/add_animated_ui`
3. `/generate_tests`
4. `/review_pr`

If feature missing:

1. `/create_feature`
2. `/add_form_flow`
3. `/add_animated_ui`
4. `/generate_tests`
5. `/review_pr`

### Bug in API-backed UI

1. `/fix_bug`
2. `/migration_check` if response may have changed
3. `/connect_design_to_apis` if wiring APIs to existing design is the issue
4. `/api_endpoint` if lower-level integration must change
5. `/generate_tests`
6. `/review_pr`

### Bug in Figma UI

1. `/fix_bug`
2. `/figma_to_screens` only if Figma comparison/rework is needed
3. `/generate_tests`
4. `/review_pr`

### Bug in image-based UI

1. `/fix_bug`
2. `/images_to_flutter_design` only if visual comparison/rework from images is needed
3. `/generate_tests`
4. `/review_pr`

### Bug in form flow

1. `/fix_bug`
2. `/add_form_flow` if architecture must be corrected
3. `/generate_tests`
4. `/review_pr`

### Backend response migration

1. `/migration_check`
2. `/connect_design_to_apis` if existing design is wired or should be wired
3. `/api_endpoint` if data layer must change
4. `/generate_tests`
5. `/review_pr`

### Security-sensitive implementation

1. `/security_check`
2. Matching workflow:
   - `/figma_to_screens`
   - `/images_to_flutter_design`
   - `/connect_design_to_apis`
   - `/api_endpoint`
   - `/add_form_flow`
   - `/fix_bug`
   - `/create_feature`
3. `/generate_tests`
4. `/review_pr`

### Refactor existing UI

1. `/refactor_safely`
2. `/generate_tests`
3. `/review_pr`

### Cleanup

1. `/cleanup`
2. `/generate_tests` if behavior/tested code changed
3. `/review_pr`

### Prepare PR

1. `/generate_tests`
2. `/review_pr`
3. `/commit_message`

### Docs after feature

1. `/write_docs`
2. `/review_pr`

## Conflict Resolution

Choose the most specific workflow first:

- Figma link + UI → `/figma_to_screens`
- Uploaded images/screenshots + UI → `/images_to_flutter_design`
- APIs + existing screen/design → `/connect_design_to_apis`
- Figma/images + APIs → design workflow first, then `/connect_design_to_apis`
- Figma + uploaded images → `/figma_to_screens` source of truth, images secondary reference
- Paginated endpoint with existing design → `/connect_design_to_apis`, then `/add_paginated_list`
- Paginated endpoint without design context → `/api_endpoint`, then `/add_paginated_list`
- Animated Figma screen → `/figma_to_screens`, then `/add_animated_ui`
- Animated image-based screen → `/images_to_flutter_design`, then `/add_animated_ui`
- API response changed → `/migration_check`, then `/connect_design_to_apis` or `/api_endpoint`
- UI bug from DTO mapping → `/fix_bug`, then `/migration_check`, then `/connect_design_to_apis`

If ambiguous, ask one concise question:

- Is this new or existing?
- Is data from API or local state?
- Is design already in app, from Figma, or uploaded images?
- Are these APIs for an existing screen or should I create it?
- Paginated or static?
- Need entrance animations?

If user asks for shortcuts that violate rules, refuse the shortcut and propose the project-standard approach.

## Final Output

```md
## Completed Workflow(s)

1. ...

## What Changed

- ...

## Design Source

- Figma: Yes / No
- Uploaded images: Yes / No
- Existing design: Yes / No

## Screens Implemented

- ...

## API Work

- APIs connected: Yes / No
- Endpoints:
  - ...

## Tests

- ...

## Review Notes

- ...

## Remaining Risks / Assumptions

- ...
```
