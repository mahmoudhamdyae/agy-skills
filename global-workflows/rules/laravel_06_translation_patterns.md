---
trigger: model_decision
description: "Laravel HMVC Clean Architecture Rule: 06_translation_patterns.md"
---

# Translation Patterns (Arabic / English)

## Option A: JSON column + manual accessor (no package)

### Migration

```php
$table->json('name');            // {'en': 'Product', 'ar': 'منتج'}
$table->json('description')->nullable();
```

### Model accessor

```php
use Illuminate\Support\Facades\App;

protected function name(): Attribute
{
    return Attribute::make(
        get: fn($value) => json_decode($value, true)[App::getLocale()]
                           ?? json_decode($value, true)['en']
                           ?? $value,
    );
}
```

### Filament form (store both)

```php
// Use name.en and name.ar as separate fields, then combine in mutateFormDataBeforeCreate
protected function mutateFormDataBeforeCreate(array $data): array
{
    $data['name'] = ['en' => $data['name_en'], 'ar' => $data['name_ar']];
    unset($data['name_en'], $data['name_ar']);
    return $data;
}
```

Or use a custom cast:

```php
protected $casts = ['name' => 'array'];
```

Then in form: `TextInput::make('name.en')` and `TextInput::make('name.ar')` work directly.

---

## Option B: spatie/laravel-translatable (recommended)

### Install

```bash
composer require spatie/laravel-translatable
```

### Model

```php
use Spatie\Translatable\HasTranslations;

class Product extends Model
{
    use HasTranslations;

    public array $translatable = ['name', 'description'];
}
```

### Migration — same as Option A (json columns)

### Usage

```php
$product->name;                      // returns current locale
$product->getTranslation('name', 'ar');
$product->setTranslation('name', 'en', 'Product');
$product->setTranslations('name', ['en' => 'Product', 'ar' => 'منتج']);
```

### Filament form with spatie

```php
// Works directly with dot notation:
TextInput::make('name.en')->label('Name (English)')->required(),
TextInput::make('name.ar')->label('الاسم بالعربي')->required()->dir('rtl'),
```

No mutateFormData needed — Filament + spatie handle it automatically.

---

## Language Switching in Filament Panel

In `PanelServiceProvider`:

```php
->renderHook(
    'panels::body.start',
    fn() => view('filament.lang-switcher'),
)
```

Or use a middleware to set locale from user preferences:

```php
// app/Http/Middleware/SetLocale.php
public function handle($request, Closure $next)
{
    $locale = auth()->user()?->locale ?? session('locale', 'en');
    App::setLocale($locale);
    return $next($request);
}
```

---

## RTL Support in Filament

In `PanelServiceProvider`:

```php
->viteTheme('resources/css/filament/admin/theme.css')
```

In CSS, detect RTL:

```css
[dir="rtl"] .fi-input {
  text-align: right;
}
```

Or use Filament's built-in:

```php
->spa()
->unsavedChangesAlerts()
->direction(fn() => app()->getLocale() === 'ar' ? 'rtl' : 'ltr') // if supported
```

---

## Translation File Naming Convention

```
Modules/{Name}/lang/
├── en/
│   ├── {module}.php       ← main translations
│   ├── validation.php     ← validation messages
│   └── notifications.php  ← notification strings
└── ar/
    ├── {module}.php
    ├── validation.php
    └── notifications.php
```

### Key naming convention

```php
// Prefer flat keys for simple strings
'name'            => 'Name',
'is_active'       => 'Active',

// Use dot notation for grouped strings
'actions.create'  => 'Create',
'actions.edit'    => 'Edit',
'actions.delete'  => 'Delete',

// Status labels
'status.pending'  => 'Pending',
'status.approved' => 'Approved',
```
