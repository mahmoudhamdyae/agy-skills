---
trigger: model_decision
description: "Laravel HMVC Clean Architecture Rule: 04_testing_standards.md"
---

## 1. Testing Mandate

Testing is **not optional**. Every feature must be accompanied by tests. This is a hard rule.

| Scope            | What to Test                                              | Tool              |
|------------------|-----------------------------------------------------------|-------------------|
| API Endpoint     | Full request/response cycle (status, structure, data)     | Pest Feature Test |
| Service Logic    | Business rules, branching, edge cases                     | Pest Unit Test    |
| Repository       | Query correctness (can use in-memory DB or mock)          | Pest Unit Test    |
| FormRequest      | Validation rules (valid, invalid, boundary cases)         | Pest Feature Test |
| Policy / Gate    | Authorization logic for all roles                         | Pest Feature Test |

## 2. Pest Test Structure

### Feature Test (API Endpoint)

```php
<?php

use App\Models\User;
use App\Models\Post;

uses(Tests\TestCase::class, Illuminate\Foundation\Testing\RefreshDatabase::class);

it('allows an authenticated user to create a post', function (): void {
    $user = User::factory()->create();

    $response = $this->actingAs($user)->postJson('/api/v1/posts', [
        'title' => 'Test Post',
        'body'  => 'Some content here.',
    ]);

    $response->assertStatus(201)
             ->assertJsonStructure(['data' => ['id', 'title', 'body']]);

    $this->assertDatabaseHas('posts', ['title' => 'Test Post', 'user_id' => $user->id]);
});

it('returns 422 when title is missing', function (): void {
    $user = User::factory()->create();

    $this->actingAs($user)->postJson('/api/v1/posts', [])
         ->assertStatus(422)
         ->assertJsonValidationErrors(['title']);
});

it('prevents unauthenticated access', function (): void {
    $this->postJson('/api/v1/posts', ['title' => 'Test'])
         ->assertStatus(401);
});
```

### Unit Test (Service)

```php
<?php

use App\Services\PostService;
use App\Repositories\PostRepository;
use Mockery;

it('creates a post and returns the model', function (): void {
    $repo = Mockery::mock(PostRepository::class);
    $repo->shouldReceive('create')->once()->andReturn(new Post(['title' => 'Test']));

    $service = new PostService($repo);
    $post = $service->create(['title' => 'Test', 'user_id' => 1]);

    expect($post->title)->toBe('Test');
});
```

## 3. Test Organization Rules

- Store Feature tests in `tests/Feature/` grouped by domain (e.g., `tests/Feature/Post/`).
- Store Unit tests in `tests/Unit/` mirroring the `app/` structure (e.g., `tests/Unit/Services/PostServiceTest.php`).
- One test file per class/endpoint (e.g., `CreatePostTest.php`, `UpdatePostTest.php`).
- Use **descriptive `it()` descriptions** — write them as readable sentences.

## 4. Always Include These Cases

For every API endpoint, always test at minimum:

- ✅ Happy path (valid data, correct response structure & status)
- ✅ Validation failure (missing/invalid fields → 422 with correct error keys)
- ✅ Unauthenticated access (→ 401)
- ✅ Unauthorized access (wrong user/role → 403)
- ✅ Not found (→ 404 for resource-based routes)

## 5. Golden Rules

- Always use `RefreshDatabase` trait in Feature tests.
- Always use Factories to create test data — never hardcode IDs or DB states.
- Mock external HTTP calls and third-party services in Unit tests.
- Never assert on raw SQL or internal implementation details — test behavior.
- Run `php artisan test` before marking any task as done.
