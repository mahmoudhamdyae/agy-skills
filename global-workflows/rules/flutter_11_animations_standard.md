---
trigger: model_decision
description: "Flutter Architecture Rule: 11_animations_standard.md"
---

# 11. Animation Standards

This document defines the mandatory pattern for entrance animations to ensure a premium, dynamic experience.

---

## 1. Core Implementation (`CustomFadeInSlide`)
All entrance animations MUST use `CustomFadeInSlide` from `lib/core/widgets/animations/`.

- **Trigger Policy**: Animations MUST trigger on every screen entry. Never restrict to "first-time".
- **Tokens**: (MANDATORY) Use tokens from `ConstantsManager`. Never hardcode durations/offsets.
    - `animationsDurationStep`: Standard duration (e.g., `800ms`).
    - `animationsDelayStep`: Delay increment (e.g., `150ms`).
    - `animationsOffset`: Slide distance (e.g., `30.he()`).

---

## 2. Animation Directions

| Direction | Movement | Recommended Usage |
| :--- | :--- | :--- |
| **`.up`** | Bottom -> Top | Main content, CTA buttons. |
| **`.down`** | Top -> Bottom | Headers, Hero images. |
| **`.start`** | Leading -> Trailing| Form fields (alternating). |
| **`.end`** | Trailing -> Leading| Form fields (alternating). |

---

## 3. Staggered Entrance Pattern
To create a sophisticated cascaded effect, increment delays using `ConstantsManager.animationsDelayStep`.

```dart
children: [
  CustomFadeInSlide(
    direction: .start,
    delay: const Duration(milliseconds: ConstantsManager.animationsDelayStep * 1),
    child: NameTextField(),
  ),
  CustomFadeInSlide(
    direction: .end,
    delay: const Duration(milliseconds: ConstantsManager.animationsDelayStep * 2),
    child: EmailTextField(),
  ),
]
```

---

## 4. Coding Standards
- **Wait for Curves**: Default is `Curves.easeOutCubic` for a premium motion profile.
- **Granularity**: Wrap only the smallest relevant UI unit to maintain performance.
- **const Usage**: (MANDATORY) Always use `const Duration` for delays with static multipliers.

---

## 5. Placement Rules
- **Sections**: Primary home for `CustomFadeInSlide` (Logic for staggered groups).
- **Widgets**: Internal animations for single units (e.g., custom list items).
- **Screens**: MUST NOT contain animation logic; they are orchestration hubs only.
