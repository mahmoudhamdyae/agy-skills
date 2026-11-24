---
trigger: model_decision
description: "Laravel HMVC Clean Architecture Rule: 05_modular_architecture.md"
---

# Cross-Module Relations & Service Patterns

## Referencing Models Across Modules

```php
// In Modules/Orders/app/Models/Order.php
use Modules\Catalog\App\Models\Product;

public function product(): BelongsTo
{
    return $this->belongsTo(Product::class);
}
```

## Service Pattern (inside module)

```php
// Modules/{Name}/app/Services/{Name}Service.php
namespace Modules\{Name}\App\Services;

use Modules\{Name}\App\Models\{Model};

class {Name}Service
{
    public function create(array $data): {Model}
    {
        return {Model}::create($data);
    }

    public function update({Model} $model, array $data): {Model}
    {
        $model->update($data);
        return $model->fresh();
    }

    public function delete({Model} $model): bool
    {
        return $model->delete();
    }
}
```

Bind in ServiceProvider if needed:

```php
$this->app->bind({Name}Service::class, fn() => new {Name}Service());
```

## Repository Pattern (optional, for complex modules)

```php
// Interface
interface {Name}RepositoryInterface
{
    public function all();
    public function find(int $id): {Model};
    public function create(array $data): {Model};
}

// Implementation
class {Name}Repository implements {Name}RepositoryInterface
{
    public function __construct(protected {Model} $model) {}

    public function all() { return $this->model->active()->latest()->get(); }
    public function find(int $id): {Model} { return $this->model->findOrFail($id); }
    public function create(array $data): {Model} { return $this->model->create($data); }
}
```

## Shared Module Resources

If multiple modules share data (e.g., a `Core` module):

```
Modules/
└── Core/
    └── app/
        ├── Models/
        │   ├── Country.php
        │   └── Currency.php
        └── Services/
            └── SettingsService.php
```

Import with full namespace:

```php
use Modules\Core\App\Models\Country;
```

## Module Events (cross-module communication)

```php
// Fire event from one module
event(new \Modules\Orders\App\Events\OrderCreated($order));

// Listen in another module's ServiceProvider
Event::listen(
    \Modules\Orders\App\Events\OrderCreated::class,
    \Modules\Notifications\App\Listeners\SendOrderNotification::class,
);
```

## Active Scope Convention

Always add to main models:

```php
public function scopeActive(Builder $query): Builder
{
    return $query->where('is_active', true);
}
```

Usage: `Product::active()->latest()->get()`

## Cross-Module Dependency Injection

To maintain decoupling while using services from other modules:
1. Define an interface (Contract) in the module's `app/Contracts` directory.
2. Bind the implementation in the module's `ServiceProvider`.
3. Type-hint the interface in the constructor of another module's service.

```php
// In Modules/Orders/app/Services/OrderService.php
namespace Modules\Orders\App\Services;

use Modules\Payments\App\Contracts\PaymentInterface;

class OrderService
{
    public function __construct(
        private readonly PaymentInterface $paymentService, // Injected from Payment module
    ) {}
}
```

## Service Provider Best Practices

- **Register Method**: Register module-specific bindings, singletons, and configurations.
  ```php
  public function register(): void
  {
      $this->app->singleton(PaymentInterface::class, StripePaymentService::class);
  }
  ```
- **Boot Method**: Load migrations, translations, views, and register listeners.
  ```php
  public function boot(): void
  {
      $this->loadMigrationsFrom(module_path($this->name, 'database/migrations'));
      $this->loadTranslationsFrom(module_path($this->name, 'lang'), $this->nameLower);
  }
  ```
- **Inter-module communication**: Always favor Events/Listeners for side effects (e.g., sending an email after an order is created) to avoid tight coupling between modules.
