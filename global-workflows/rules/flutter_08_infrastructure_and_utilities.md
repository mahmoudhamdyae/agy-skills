---
trigger: model_decision
description: "Flutter Architecture Rule: 08_infrastructure_and_utilities.md"
---

# 08. Infrastructure and Utilities

This document defines how to interact with managers, safety parsing, and navigation helpers.

---

## 1. Core Utilities

| Utility | Purpose | Mandatory Usage |
| :--- | :--- | :--- |
| **`Log`** | Console Logging | Use `Log.success`, `.error`, `.warning`. **Never use raw print.** |
| **`ParseUtils`** | Data Safety | Use `ensureInt`, `ensureDouble`, `ensureString` inside all `fromJson` factories. |
| **`Navigation`** | Screen Routing | Use `context.push`, `.go`, `.pop`. **Never use raw Navigator.** |

---

## 2. Interaction Managers (`lib/core/helpers/`)
Always use these pre-built managers to maintain consistent UI/UX.

| Manager | Purpose | Key Function |
| :--- | :--- | :--- |
| **`DialogsManager`** | Popups | `showLoadingDialog`, `showSuccess`, `showError`, `showDelDialog`. |
| **`SnackBarsManager`** | Inline Alerts | `showSuccessSnackBar`, `showErrorSnackBar`. |
| **`BottomSheetsManager`**| Sheets | `showBottomSheet`, `showFileBottomSheet`. |
| **`PermissionsManager`** | OS Rights | `checkAndRequestPermission`. |
| **`PickersManager`** | Media | `pickImageFromGallery`, `pickFiles`. |
| **`LauncherManager`** | External Apps | `launchWebUrl`, `launchWhatsApp`, `launchDialer`, `launchGoogleMap`. |
| **`Pagination`** | List Logic | `PaginationController` (Manages ScrollController & loading state). |

---

## 3. Localization and Assets
- **`StringsManager`**: (MANDATORY) All labels and messages must be stored here (`key.tr()`). No hardcoded strings.
- **`AssetsManager`**: Centralized paths for SVG, Images, and Lottie animations.
- **`FcmManager`**: Handles Firebase Cloud Messaging and background notifications.

---

## 4. Common Helpers
- **`HelperFunctions`**: `unFocusKeyboard()` (MANDATORY on submits), `generateTimeBasedId()`.
- **`Formatter`**: Methods for Date/Time and Currency formatting.
- **`ConvertersManager`**: Handles Base64, Hex, and unit conversions.

---

## 5. Global Extensions (`lib/core/extensions/`)

### String & DateTime
- **`String`**: `isEmptyOrNull`, `isNotBlank`, `copy(context)`, `share()`, `toAge()`.
- **`DateTime`**: `toYMD()`, `toHM()`, `timeAgo()`, `isYesterday`, `isTomorrow`.

### num & Widget
- **`num` (Spacing)**: `ph`, `pw` (Vertical/Horizontal SizedBox), `sliverPh`, `sliverPw`.
- **`Widget`**: `.paddingAll(16)`, `.center()`, `.expand()`, `.visible(bool)`, **`.onTap(() {})`**.
