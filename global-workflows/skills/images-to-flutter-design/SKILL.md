---
name: images-to-flutter-design
description: >-
  Flutter Clean Architecture & S-S-W workflow: Convert uploaded UI images, screenshots, or mockups into production-ready Flutter UI code while following the project's Clean Architecture, S-S-W pattern, Core Foundation, responsive styling, assets, tests, and review standards.
---

# Images to Flutter Design Workflow

## Goal

Convert uploaded UI images, screenshots, or mockups into production-ready Flutter UI code while following the project's Clean Architecture, S-S-W pattern, Core Foundation, responsive styling, assets, tests, and review standards.

Use this workflow when the user uploads image(s) and asks to convert them into Flutter design/code.

## Supported Inputs

- Uploaded PNG/JPG/WebP screenshots.
- UI mockup images.
- App screen screenshots.
- Design reference images.
- Multiple images for the same feature or flow.

If the image is unclear, low-resolution, cropped, or contains multiple screens, ask one concise clarification question only if needed.

## Mandatory Rules

- Follow Plan → Implement → Review.
- Do not implement blindly.
- Inspect the uploaded image(s) and existing codebase first.
- Wait for approval before editing files.
- Preserve the visual design as closely as possible.
- Use Clean Architecture and S-S-W:
  - Screen = orchestration only.
  - Section = layout/state/interactions.
  - Widget = pure UI.
- Use Core Foundation First.
- Prefer project widgets over raw Flutter widgets.
- Use:
  - `CustomScaffold`
  - `CustomText`
  - `CustomButton`
  - `CustomTextField`
  - `CustomAppBar`
  - `StatesScreen/List/Grid` when state is needed.
- Use responsive extensions:
  - `.wi()`
  - `.he()`
  - `.rad()`
  - `.sp()`
  - `.ph`
  - `.pw`
- Do not use raw `Colors.xxx`; use context theme/color extensions.
- Do not hardcode user-facing strings; use `StringsManager`.
- Use `.onTap()` for custom taps.
- Use `CustomFadeInSlide` only if animation is requested or clearly implied.
- Add/update Widget and Golden tests where applicable.
- End with `/review_pr`.

## Related Workflows

Call when needed:

- `/create_feature`
- `/add_form_flow`
- `/add_paginated_list`
- `/add_animated_ui`
- `/generate_tests`
- `/review_pr`
- `/cleanup`

## Workspace

Create a temporary workspace at git root:

```bash
mkdir -p .ui-workspace/$FEATURE/{input_images,app_screenshots,goldens,notes}
grep -q "^\.ui-workspace/$" .git/info/exclude || echo ".ui-workspace/" >> .git/info/exclude
```

Never commit `.ui-workspace/`.

Copy or reference uploaded images into:

```text
.ui-workspace/$FEATURE/input_images/
```

## 1. Plan

1. Identify feature/screen name from user request, image content, route, branch, or existing code.
2. Inspect uploaded image(s):
   - screen count
   - device size/aspect ratio
   - layout hierarchy
   - components
   - text
   - colors
   - spacing
   - images/icons
   - forms/buttons/lists/cards
   - states if visible
3. Inspect existing Flutter project for:
   - similar screens
   - design system widgets
   - theme extensions
   - typography conventions
   - asset structure
   - feature folder pattern
4. Classify the task:
   - New feature/screen.
   - Existing screen redesign.
   - Static UI only.
   - Form screen.
   - List/grid screen.
   - Paginated screen.
   - Animated screen.
5. Select required workflows:
   - New feature → `/create_feature`
   - Form → `/add_form_flow`
   - Paginated list → `/add_paginated_list`
   - Animation → `/add_animated_ui`
   - Tests → `/generate_tests`
   - Final review → `/review_pr`
6. Output plan and wait for approval.

Use output:

```md
## Image to Flutter Plan

### Target Feature

...

### Target Screen(s)

...

### Detected UI Type

Static / Form / List / Paginated / Redesign / Multi-screen flow

### Selected Workflow(s)

1. ...

### Visual Notes

- Layout:
- Typography:
- Colors:
- Spacing:
- Assets/icons:
- Interactions:

### Files Likely to Change

- ...

### Assumptions

- ...

### Approval Needed

Yes
```

## 2. Visual Breakdown

Before coding, write a concise visual spec from the image.

Include:

- screen background
- app bar/header
- main sections
- cards/containers
- buttons
- input fields
- lists/grids
- icons/images
- bottom navigation or tabs
- empty/loading/error areas if implied
- responsive behavior

Example:

```md
## Visual Spec

- Background: light surface.
- Header: title at top-left, action icon top-right.
- Main content: vertical list of rounded cards.
- CTA: fixed bottom button.
- Spacing: large outer padding, medium card gaps.
```

## 3. Extract Design Values

Approximate values from the image while matching project conventions.

Document:

```md
## Design Values

- Device baseline: 390x844 unless image suggests otherwise.
- Outer padding: ...
- Main gap: ...
- Card radius: ...
- Button height: ...
- Font sizes: ...
- Font weights: ...
- Colors: use nearest project theme token where possible.
```

Rules:

- Prefer existing theme/context colors over literal hex.
- Use literal design colors only when no matching theme token exists, and consider adding to theme only with approval.
- Use `.wi()`, `.he()`, `.rad()`, `.sp()` for dimensions.
- Use `.ph` and `.pw` for spacing.

## 4. Asset Strategy

If image contains icons/photos/illustrations:

1. Search existing assets first.
2. Reuse project assets when visually close.
3. If the uploaded image contains a unique asset that must be extracted, ask for source asset or use the uploaded image only as reference.
4. Do not crop/export assets from screenshots unless explicitly approved.
5. If new assets are added:
   - use snake_case names
   - put them in the existing asset structure
   - update `pubspec.yaml` only if needed
   - document asset mapping in `.ui-workspace/$FEATURE/notes/asset_mapping.md`

## 5. Implement Flutter UI

### Screen

- Use `CustomScaffold`.
- Keep orchestration only.
- No business logic.
- No heavy layout details.
- No direct `BlocBuilder` in Screen build.

### Section

- Build main layout composition.
- Put `BlocBuilder`, `BlocListener`, navigation, dialogs, and Cubit calls here if state exists.
- Use `StatesScreen/List/Grid` for large state handling.

### Widget

- Pure UI only.
- Constructor params for data/callbacks.
- No Cubit/Bloc access.
- One class per file.
- Prefer `StatelessWidget`.

### Styling

- Use project typography and chain modifiers.
- Use context colors.
- Use project widgets.
- Use responsive/spacing extensions.
- Extract repeated UI into widgets.
- Avoid helper functions returning widgets.

## 6. Forms

If the image shows inputs or submit flow, call `/add_form_flow`.

Rules:

- Controllers and `GlobalKey<FormState>` live in Cubit/Bloc.
- Use project fields:
  - `CustomTextField`
  - `EmailTextField`
  - `PasswordTextField`
  - `PhoneTextField`
- Use validators from project validation layer.
- Use `validateAndScroll()`.
- Call `HelperFunctions.unFocusKeyboard()` on submit.
- Use `CustomButton`.

## 7. Lists and Pagination

If the image shows static list/cards:

- Use pure widgets and fake data first if no API is provided.
- Keep data passed through params.

If the image implies infinite scrolling or backend list:

- Call `/add_paginated_list`.
- Use `PaginatedResult<T>`, `PaginationMixin`, `PaginationController`, and `StatesScreenList/Grid`.

## 8. Animations

If user asks for animation or design clearly needs entrance animation:

- Call `/add_animated_ui`.
- Use `CustomFadeInSlide`.
- Use `ConstantsManager` animation tokens.
- Put staggered logic in Sections.
- Do not hardcode durations/delays/offsets.

## 9. Tests

Call `/generate_tests`.

Add/update:

- Widget tests for the screen/sections/widgets.
- Golden tests for visual regression.
- Bloc/Cubit tests if state exists.
- Form tests if inputs exist.
- Pagination tests if list is paginated.

Golden test guidance:

```dart
testWidgets('screen matches uploaded design reference', (tester) async {
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

## 10. App Screenshot and Visual Comparison

Capture app screenshot if simulator/device is available.

iOS:

```bash
xcrun simctl io booted screenshot .ui-workspace/$FEATURE/app_screenshots/ss_$(date +%Y-%m-%d_%H-%M-%S)_screen.png
```

Android:

```bash
adb shell screencap -p > .ui-workspace/$FEATURE/app_screenshots/ss_$(date +%Y-%m-%d_%H-%M-%S)_screen.png
```

Compare uploaded reference image with app screenshot.

Check:

- layout position
- text size/weight
- colors
- spacing
- radius
- shadows
- icon/image placement
- scroll behavior
- overflow issues

Fix order:

1. layout/constraints
2. typography
3. colors
4. spacing
5. assets/icons
6. fine details

Repeat:

```text
Compare → Fix → Test → Screenshot → Compare
```

## 11. Review

Call `/review_pr`.

Verify:

- Screen/Section/Widget boundaries.
- Project widgets and extensions used.
- No raw colors.
- No hardcoded user strings.
- No business logic in UI widgets.
- No unnecessary files.
- Responsive behavior is acceptable.
- Tests/goldens added or updated.
- Uploaded image was used as reference.
- `.ui-workspace/` not committed.

## Final Output

```md
## Completed Workflow(s)

1. ...

## Implemented From Images

- ...

## Target Feature / Screens

- ...

## Files Changed

- ...

## Visual Match Notes

- ...

## Tests

- ...

## App Screenshots

- `.ui-workspace/{Feature}/app_screenshots/...`

## Remaining Differences / Assumptions

- ...
```
