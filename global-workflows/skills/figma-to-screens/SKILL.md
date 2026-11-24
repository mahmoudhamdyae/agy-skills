---
name: figma-to-screens
description: >-
  Flutter Clean Architecture & S-S-W workflow: Convert one or more Figma screens into production-ready Flutter UI following project architecture, S-S-W, Core Foundation, asset conventions, tests, and visual matching.
---

# Figma to Flutter Screens

## Goal

Convert one or more Figma screens into production-ready Flutter UI following project architecture, S-S-W, Core Foundation, asset conventions, tests, and visual matching.

Use when the user provides a Figma link and asks to implement screen(s) in Flutter.

## Inputs

- Figma URL.
- Feature name if known.
- Target screen names if multiple.
- Scope:
  - new feature
  - update existing feature
  - UI-only
  - UI + API
    If unclear, infer from design, branch, route, or code context. Ask one short question only if unsafe.

## Mandatory Rules

- Plan → Implement → Review.
- Inspect codebase and propose plan before editing.
- Wait for approval.
- Clean Architecture and S-S-W.
- Screens: orchestration only, usually `StatelessWidget`.
- Sections: layout grouping, Bloc builders/listeners, interactions, navigation/dialogs.
- Widgets: pure UI, params/callbacks only.
- Use Core Foundation first.
- Prefer project widgets/extensions over raw Flutter.
- Use `CustomScaffold`, `CustomText`, `CustomButton`, `CustomTextField`, `StatesScreen/List/Grid`.
- Use `.ph`, `.pw`, `.wi()`, `.he()`, `.rad()`, `.sp()`.
- No raw `Colors.xxx`; use context theme/color extensions.
- No hardcoded user strings; use `StringsManager`.
- Use `.onTap()` for custom taps.
- Use `CustomFadeInSlide` when motion is needed.
- Do not copy generated Figma code directly; use as reference only.
- Add/update Unit, Bloc, Widget, and Golden tests as applicable.

## Related Workflows

Use as needed:

- `/create_feature`
- `/api_endpoint`
- `/add_form_flow`
- `/add_paginated_list`
- `/add_animated_ui`
- `/generate_tests`
- `/review_pr`

## Figma API Server

Verify:

```bash
curl -s http://localhost:3001/health || echo "Server not running"
```

Server must run at `http://localhost:3001`.
If missing:

```bash
mkdir -p ~/Documents
git clone https://github.com/prateekmedia/FigmaToCode-RestApi ~/Documents/figma-api
```

Tell user to follow `~/Documents/figma-api/README`, set `FIGMA_TOKEN`, and start port `3001`. Stop until confirmed.

## Workspace

At git root:

```bash
mkdir -p .ui-workspace/$FEATURE/{figma_screenshots,figma_images,figma_code,app_screenshots}
grep -q "^\.ui-workspace/$" .git/info/exclude || echo ".ui-workspace/" >> .git/info/exclude
```

Never commit `.ui-workspace/`.

## 1. Plan

1. Read Figma URL and infer feature/screen.
2. Inspect existing project structure and similar UI.
3. Classify:
   - New feature
   - Existing feature update
   - UI-only
   - UI + API/state
   - Form
   - Paginated list
   - Animated screen
4. Identify target files:
   - `lib/features/{feature}/presentation/screens/`
   - `sections/`
   - `widgets/`
   - `domain/`
   - `data/`
   - `test/features/{feature}/`
5. Select workflows:
   - New feature → `/create_feature`
   - API-backed → `/api_endpoint`
   - Form → `/add_form_flow`
   - Pagination → `/add_paginated_list`
   - Animation → `/add_animated_ui`
   - Tests → `/generate_tests`
   - Final → `/review_pr`
6. Output plan and wait approval.

Use output:

```md
## Detected Figma Task

...

## Selected Workflow(s)

1. ...

## Figma Extraction Plan

...

## Flutter Implementation Plan

...

## Approval Needed

Yes
```

## 2. Prepare Extraction

After approval:

```bash
export FIGMA_URL="PASTE_FIGMA_URL_HERE"
export FEATURE="feature_name"
curl -s http://localhost:3001/health
```

If unavailable, stop and report setup steps.

## 3. Asset Strategy

Before API calls:

```bash
ls -la assets/ || true
find assets -maxdepth 2 -type d 2>/dev/null || true
grep -r "Image\.asset.*scale:" lib/ || true
```

Choose scales:

- Existing `assets/2x`, `3x`, `4x` → download existing scales only.
- Frequent `scale: 3` → `["3x"]`.
- Frequent `scale: 4` → `["4x"]`.
- No convention → default `["3x"]`.

Output:

```md
## Asset Scale Decision

Selected scales: [...]
Reason: ...
```

## 4. Extract Figma Screenshot and Reference Code

Screenshot:

```bash
curl -X POST http://localhost:3001/api/screenshot   -H "Content-Type: application/json"   -d "{
    "url":"$FIGMA_URL",
    "format":"png",
    "scale":2,
    "saveToFile":true,
    "directory":".ui-workspace/$FEATURE/figma_screenshots"
  }"
```

Convert, with selected scales:

```bash
curl -X POST http://localhost:3001/api/convert   -H "Content-Type: application/json"   -d "{
    "url":"$FIGMA_URL",
    "settings":{"framework":"Flutter"},
    "exportImages":true,
    "exportImagesOptions":{
      "scales":["3x"],
      "directory":".ui-workspace/$FEATURE/figma_images"
    },
    "output":{
      "saveToFile":true,
      "directory":".ui-workspace/$FEATURE/figma_code"
    }
  }"
```

Outputs:

- screenshots: `.ui-workspace/$FEATURE/figma_screenshots/`
- reference code: `.ui-workspace/$FEATURE/figma_code/`
- assets: `.ui-workspace/$FEATURE/figma_images/`

## 5. Review Extracted Materials

Inspect:

- Screenshot
- Generated reference code
- Assets
- Text styles
- Colors
- Spacing
- Dimensions
- Layout hierarchy
- Repeated components
- Icons/images

Use generated code only for values/reference, not direct production copy.

## 6. Implement Flutter UI

If new feature, call `/create_feature`.

Structure:

```text
lib/features/{feature}/
├── data/
├── domain/
└── presentation/
    ├── screens/
    ├── sections/
    └── widgets/
```

### Screen

- Use `CustomScaffold`.
- Orchestration only.
- Provide Bloc/Cubit if needed.
- No detailed layout or business logic.
- No direct `BlocBuilder` in Screen build.

### Section

- Compose layout.
- Hold BlocBuilder/Listener.
- Handle navigation/dialogs/Cubit calls.
- Use `StatesScreen/List/Grid` where needed.

### Widget

- Pure UI.
- No Bloc/Cubit.
- Data/callbacks via constructor.
- One class per file.
- Prefer `StatelessWidget`.

### Styling

- Use `context.displayLarge/titleLarge/bodyMedium` and chain modifiers.
- Use `.wi()`, `.he()`, `.rad()`, `.sp()`, `.ph`, `.pw`.
- Use project widgets and context colors.
- No raw `Colors.xxx`.

### Animation

If needed, call `/add_animated_ui`.
Use `CustomFadeInSlide`, `ConstantsManager` animation tokens, and keep stagger logic in Sections.

### Forms

If form exists, call `/add_form_flow`.
Controllers/FormKey live in Bloc/Cubit. Use `validateAndScroll()`, `HelperFunctions.unFocusKeyboard()`, project fields/buttons/validators.

### Pagination

If infinite list/grid, call `/add_paginated_list`.
Use `PaginatedResult<T>`, `PaginationMixin`, `PaginationController`, and `StatesScreenList/Grid`.

## 7. Assets

1. Identify required assets from generated code/screenshot.
2. Copy only used assets.
3. Rename snake_case and descriptive:

```bash
cp .ui-workspace/$FEATURE/figma_images/3x/123:456_avatar.png assets/profile_avatar.png
```

4. Save mapping:

```json
{
  "123:456_avatar.png": "assets/profile_avatar.png"
}
```

at `.ui-workspace/$FEATURE/figma_images/mapping.json`. 5. Update `pubspec.yaml` only if needed.

## 8. Tests

Call `/generate_tests`.
Add/update:

- Widget tests
- Golden tests
- Bloc/Cubit tests if state exists
- Unit tests if domain/data exists

Golden rules:

- Match Figma device size when known.
- Use stable wrappers and fake images.
- Capture multiple scroll states when needed.

Example:

```dart
testWidgets('feature screen matches figma design', (tester) async {
  await tester.binding.setSurfaceSize(const Size(390, 844));
  await tester.pumpApp(const FeatureScreen());
  await expectLater(
    find.byType(FeatureScreen),
    matchesGoldenFile('goldens/feature_screen.png'),
  );
});
```

Run:

```bash
flutter test --update-goldens
flutter test
```

## 9. App Screenshots

iOS simulator:

```bash
xcrun simctl io booted screenshot .ui-workspace/$FEATURE/app_screenshots/ss_$(date +%Y-%m-%d_%H-%M-%S)_screen.png
```

Android:

```bash
adb shell screencap -p > .ui-workspace/$FEATURE/app_screenshots/ss_$(date +%Y-%m-%d_%H-%M-%S)_screen.png
```

Real iOS:

```bash
~/Documents/scripts/ios_screenshot.sh .ui-workspace/$FEATURE/app_screenshots/ss_$(date +%Y-%m-%d_%H-%M-%S)_screen.png
```

## 10. Visual Comparison

Compare Figma vs app screenshots:

- layout
- typography
- colors
- spacing
- padding/margins
- assets
- borders/shadows/radius
- scroll behavior
- loading/empty/error/success states

Fix order:

1. layout/constraints
2. typography
3. colors
4. assets
5. spacing
6. fine details

Repeat: Compare → Fix → Retest → Screenshot → Compare.

## 11. Final Review

Call `/review_pr`.
Verify:

- S-S-W
- Core Foundation
- no raw colors
- no hardcoded strings
- responsive extensions
- asset naming/mapping
- tests/goldens
- Figma/app screenshots compared
- generated code not copied directly
- `.ui-workspace/` not committed

## Final Output

```md
## Completed Workflow(s)

1. ...

## Implemented Screens

- ...

## Figma References Used

- Screenshot: `.ui-workspace/{Feature}/figma_screenshots/...`
- Reference code: `.ui-workspace/{Feature}/figma_code/...`
- Assets: `.ui-workspace/{Feature}/figma_images/...`

## App Screenshots

- `.ui-workspace/{Feature}/app_screenshots/...`

## Asset Mapping

- `.ui-workspace/{Feature}/figma_images/mapping.json`

## Tests

- ...

## Visual Match Notes

- ...

## Remaining Differences / Assumptions

- ...
```
