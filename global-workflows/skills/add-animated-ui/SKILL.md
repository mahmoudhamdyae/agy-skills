---
name: add-animated-ui
description: >-
  Flutter Clean Architecture & S-S-W workflow: Add entrance animations to a screen, section, or widget using the project's mandatory animation standard.
---

# Add Animated UI

## Goal

Add entrance animations to a screen, section, or widget using the project's mandatory animation standard.

## Mandatory Rules

- Use `CustomFadeInSlide`.
- Use animation tokens from `ConstantsManager`.
- Never hardcode durations, delays, or offsets.
- Animations must trigger on every screen entry.
- Place staggered animation logic in Sections.
- Screens must not contain animation logic.
- Wrap the smallest relevant UI unit for performance.

## Workflow

### 1. Plan

1. Inspect the target UI.
2. Identify the proper animation owner:
   - Section for staggered groups.
   - Widget for single internal animation.
   - Never Screen for animation logic.
3. Identify animation order and direction:
   - `.down` for headers or hero content.
   - `.up` for main content and CTA buttons.
   - `.start` and `.end` for alternating form fields.
4. Propose the animation plan and wait for approval.

### 2. Implement

After approval only:

1. Wrap target units with `CustomFadeInSlide`.
2. Use:
   - `ConstantsManager.animationsDurationStep`
   - `ConstantsManager.animationsDelayStep`
   - `ConstantsManager.animationsOffset`
3. Use `const Duration` for static delay multipliers.
4. Preserve existing UI behavior.
5. Avoid unnecessary animation wrappers.

### 3. Review

1. Verify animation placement follows S-S-W.
2. Verify no hardcoded animation values.
3. Verify performance is not harmed by over-wrapping.
4. Run widget tests if affected.
5. Summarize animation changes.
