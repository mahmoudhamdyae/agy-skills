---
trigger: model_decision
description: "Laravel HMVC Clean Architecture Rule: 02_code_style_best_practices.md"
---

## 1. PHP and Laravel Coding Style

- Follow **PSR-12** and Laravel's official coding standards.
- Use **strict type hinting** for all method parameters and return types (PHP 8.2+):
  ```php
  // ❌
  function getUser($id) { ... }

  // ✅
  public function getUser(int $id): User { ... }
  ```
- Use **Constructor Property Promotion** for clean dependency injection:
  ```php
  public function __construct(
      private readonly PostRepository $postRepository,
  ) {}
  ```
- Use `readonly` properties for values that must not change after construction.
- Keep methods small and focused on a single responsibility.
- Use clear, descriptive names for variables, methods, and classes.
- Avoid code duplication (DRY). Extract logic into Services, Traits, or Actions as appropriate.
- **Imports (FQCN)**: **NEVER** use fully qualified class names directly in the code (e.g., `\App\Models\User`). Always use the `use` statement at the top of the file.
  ```php
  // ❌
  $user = \App\Models\User::find(1);

  // ✅
  use App\Models\User;
  $user = User::find(1);
  ```


## 2. Laravel-Specific Best Practices

- **Environment access**: **NEVER** use `env()` outside of `config/*.php` files. Use `config('key')` everywhere else.
- **Global helpers**: Avoid `app()`, `resolve()`, and global helper functions inside business logic — prefer constructor injection.
- **PHPDoc**: Add doc blocks only when type hints alone are insufficient or when the logic is genuinely complex.
- **Enums**: Prefer PHP 8.1+ backed Enums over string/integer magic constants.
  ```php
  enum PostStatus: string
  {
      case Draft     = 'draft';
      case Published = 'published';
  }
  ```
- **Named Arguments**: Use for readability when calling functions with multiple parameters.
- **Match expressions**: Prefer `match` over long `if/elseif` chains for exhaustive value mapping.

## 3. Error Handling

- **Custom Exceptions**: Create domain-specific exceptions for business logic failures:
  ```php
  class PostAlreadyPublishedException extends RuntimeException
  {
      public function __construct()
      {
          parent::__construct('This post has already been published.');
      }
  }
  ```
- **Global Handler**: Register exception rendering in `bootstrap/app.php` (Laravel 11+) or `app/Exceptions/Handler.php`.
- **HTTP Status Codes**: Return the correct code. Never return 200 for errors. **All error responses must follow the Unified API Response structure** (`success: false`, `message`, `data`):
  - `422` — Validation failure (data should contain the error detail)
  - `401` — Unauthenticated
  - `403` — Unauthorized (authenticated but not permitted)
  - `404` — Resource not found
  - `500` — Unexpected server error (never expose stack traces in production)
- **Never let exceptions fail silently**. If you catch an exception, handle it meaningfully or re-throw it.

## 4. Security Standards

- **Authorization**: Use **Policies** (or Gates for simple cases) for all resource-level authorization. Never put auth checks inside business logic.
- **Passwords**: Always use `Hash::make()`. Never store plain text. Never compare with `==`.
- **Sensitive data**: Never log tokens, passwords, or personal data. Never expose them in error messages.
- **Mass Assignment**: Always define `$fillable` explicitly. Avoid `$guarded = []`.
- **Raw SQL**: Never use raw SQL without bound parameters (`DB::statement()` with bindings is acceptable).
- **Rate Limiting**: Apply `throttle` middleware to all public-facing API endpoints.

## 5. Logging

- Use Laravel's `Log` facade, not `dd()`, `dump()`, `var_dump()`, or `print_r()`.
- **Never** leave debug statements in production code. This is a hard rule.
- Log at the appropriate level:
  - `Log::info()` — routine business events.
  - `Log::warning()` — unexpected but recoverable situations.
  - `Log::error()` — failures that require attention.
  - `Log::debug()` — development-only details (ensure these don't reach production log channels).
- Log meaningful context, not just a string:
  ```php
  Log::error('Payment failed', ['user_id' => $user->id, 'amount' => $amount]);
  ```

## 6. Git and PR Conventions

- **Branch naming**: use `kebab-case`, prefixed by type:
  - `feature/post-creation`
  - `fix/user-auth-token`
  - `refactor/post-repository`
  - `chore/update-dependencies`
- **Commit messages**: imperative mood, concise, and descriptive:
  - ✅ `Add post creation endpoint with validation`
  - ❌ `Added some stuff` / `fix`
- **PR description** must include:
  - The purpose of the change.
  - Architectural decisions made.
  - Verification: which tests were run and passed.
  - Any potential side effects on existing behavior.

## 7. 2026 Standards

- Target PHP 8.4+ features where applicable (readonly classes, property hooks when stable).
- Avoid deprecated Laravel APIs. Always check the upgrade guide for the active version.
- When two approaches are viable, prefer the one with broader community adoption and long-term stability.
