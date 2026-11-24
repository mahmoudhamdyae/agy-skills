---
trigger: model_decision
description: "Laravel HMVC Clean Architecture Rule: 03_database_conventions.md"
---

## 1. Mandatory Components for Every New Table/Model

For **every** new table/model, you **MUST** provide all of the following. No exceptions.

| Artifact    | Location                             | Requirement                                          |
|-------------|--------------------------------------|------------------------------------------------------|
| Migration   | `database/migrations/`               | Foreign keys, indexes, proper column types           |
| Model       | `app/Models/`                        | `$fillable`, `$casts`, typed relationship methods    |
| Factory     | `database/factories/`                | **Mandatory**: Use realistic data with `fake()`      |
| Seeder      | `database/seeders/`                  | **Mandatory**: Uses Factory; Must be kept up-to-date |

### Model Template

```php
class Post extends Model
{
    use HasFactory, SoftDeletes;

    protected $fillable = ['title', 'user_id', 'is_active'];

    protected $casts = [
        'is_active' => 'boolean',
        'published_at' => 'datetime',
    ];

    // Scopes
    public function scopeActive(Builder $query): Builder
    {
        return $query->where('is_active', true);
    }

    // Typed relationships
    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }
}
```

### Seeder Registration

Always register new Seeders in `DatabaseSeeder.php`. Any change or addition to the models **MUST** be reflected in its corresponding Seeder immediately to keep the dashboard data valid.

```php
public function run(): void
{
    $this->call([
        UserSeeder::class,
        PostSeeder::class, // ← add every new seeder here
    ]);
}
```

## 2. Migration Conventions

- **Foreign Keys**: Always use the constrained pattern:
  ```php
  $table->foreignId('user_id')->constrained()->cascadeOnDelete();
  ```
- **Soft Deletes**: Use `$table->softDeletes()` by default on all main entities.
- **Indexing**: Index every column used in `WHERE`, `ORDER BY`, `JOIN`, or `GROUP BY`:
  ```php
  $table->index(['user_id', 'is_active']); // composite index where needed
  ```
- **Timestamps**: Always include `$table->timestamps()`.
- **Naming**: Table names are `snake_case` and plural. Model names are `PascalCase` and singular.

## 3. Eloquent Best Practices

- **Eager Loading**: Always use `with()` to eliminate N+1 query problems.
  ```php
  // ❌ N+1
  Post::all()->each(fn($p) => $p->user->name);

  // ✅ Eager load
  Post::with('user')->get();
  ```
- **Chunking**: Use `chunk()` or `lazy()` for large dataset processing. Never `->all()` on large tables.
- **Scopes**: Add `scopeActive()` to every model that has an `is_active` flag.
- **Casts**: Always define `$casts` for booleans, datetimes, enums, and JSON columns.

## 4. Database Transactions

Always wrap multi-step write operations in a transaction:

```php
DB::transaction(function () use ($data): void {
    $user = User::create($data['user']);
    $user->profile()->create($data['profile']);
});
```

## 5. Performance and Caching

- **Indexing**: Ensure all foreign keys and frequently filtered/sorted columns are indexed in migrations.
- **Caching**: Recommend Redis/Cache for data that is read frequently and changes rarely.
- **Query Optimization**: Use `select()` to fetch only needed columns. Avoid `SELECT *` on large tables.
- **Chunking**: Use `chunk()` or `cursor()` for bulk processing operations.
