---
trigger: model_decision
description: "Laravel HMVC Clean Architecture Rule: 08_main_skill.md"
---

# Laravel + Filament + HMVC (nWidart) Skill

## Stack Overview

- **Laravel** 10/11
- **HMVC**: `nWidart/laravel-modules` — modules live in `Modules/`
- **Admin Panel**: Filament v3 (panel config may vary per project — always ask if unsure)
- **i18n**: Arabic (`ar`) + English (`en`) — bilingual throughout

---

## 1. Module Structure (nWidart Standard)

When creating or referencing a module, always follow this structure:

```
Modules/
└── {ModuleName}/
    ├── app/
    │   ├── Http/
    │   │   ├── Controllers/
    │   │   └── Requests/
    │   ├── Models/
    │   ├── Services/
    │   ├── Repositories/
    │   └── Filament/
    │       ├── Resources/
    │       │   └── {Model}Resource/
    │       │       └── Pages/
    │       └── Pages/          ← custom standalone pages
    ├── config/
    ├── database/
    │   ├── factories/
    │   ├── migrations/
    │   └── seeders/
    ├── lang/
    │   ├── ar/
    │   │   └── {module}.php
    │   └── en/
    │       └── {module}.php
    ├── routes/
    │   ├── web.php
    │   └── api.php
    ├── resources/
    │   └── views/
    ├── tests/
    │   ├── Feature/
    │   └── Unit/
    └── module.json
```

> **Filament lives inside the module** at `Modules/{Name}/app/Filament/` — never in the app root.
> **Repositories live inside the module** at `Modules/{Name}/app/Repositories/` — never query Eloquent directly in a Service.

---

## 2. Creating a New Module

### Command

```bash
php artisan module:make {ModuleName}
```

### Post-creation checklist

- [ ] Register Filament plugin for this module (see Section 4)
- [ ] Add migration path to `config/modules.php` if needed
- [ ] Create `lang/ar/{module}.php` and `lang/en/{module}.php`
- [ ] Add module service provider if custom boot logic needed
- [ ] Create Factory for every Model in `database/factories/`
- [ ] Create Seeder using the Factory in `database/seeders/`
- [ ] Register the Seeder in the module's main Seeder
- [ ] Write Feature tests for every API endpoint in `tests/Feature/`
- [ ] Write Unit tests for every Service in `tests/Unit/`

---

## 3. Model + Migration + Relations

### Model (inside module)

```php
// Modules/{Name}/app/Models/{Model}.php
namespace Modules\{Name}\App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\SoftDeletes;

class {Model} extends Model
{
    use HasFactory, SoftDeletes;

    protected $fillable = [
        // list fields
    ];

    protected $casts = [
        // e.g. 'is_active' => 'boolean',
    ];

    // Relations go here
}
```

### Migration

```bash
php artisan module:make-migration create_{table}_table {ModuleName}
```

Migration file pattern:

```php
Schema::create('{table}', function (Blueprint $table) {
    $table->id();
    // translatable columns: use json type for ar/en
    $table->json('name');        // {'ar': '...', 'en': '...'}
    $table->json('description')->nullable();
    $table->boolean('is_active')->default(true);
    $table->timestamps();
    $table->softDeletes();
});
```

> **Translatable fields**: store as `json` column. Use `spatie/laravel-translatable` if available.

### Common Relations

```php
// BelongsTo
public function category(): BelongsTo
{
    return $this->belongsTo(Category::class);
}

// HasMany
public function items(): HasMany
{
    return $this->hasMany(Item::class);
}

// BelongsToMany (with pivot)
public function tags(): BelongsToMany
{
    return $this->belongsToMany(Tag::class)->withTimestamps();
}
```

---

## 4. Filament Resource Inside a Module

### Generate command

```bash
php artisan module:make-filament-resource {Model} {ModuleName}
# or manually scaffold — see structure below
```

### Resource class skeleton

```php
// Modules/{Name}/app/Filament/Resources/{Model}Resource.php
namespace Modules\{Name}\App\Filament\Resources;

use Filament\Resources\Resource;
use Modules\{Name}\App\Models\{Model};
use Modules\{Name}\App\Filament\Resources\{Model}Resource\Pages;

class {Model}Resource extends Resource
{
    protected static ?string $model = {Model}::class;
    protected static ?string $navigationIcon = 'heroicon-o-rectangle-stack';

    // Navigation label — bilingual
    public static function getNavigationLabel(): string
    {
        return __('module-name::{model}.plural');
    }

    public static function getModelLabel(): string
    {
        return __('module-name::{model}.singular');
    }

    public static function form(Form $form): Form
    {
        return $form->schema([
            // See Section 5: Forms
        ]);
    }

    public static function table(Table $table): Table
    {
        return $table->columns([
            // See Section 5: Tables
        ]);
    }

    public static function getPages(): array
    {
        return [
            'index'  => Pages\List{Model}s::route('/'),
            'create' => Pages\Create{Model}::route('/create'),
            'edit'   => Pages\Edit{Model}::route('/{record}/edit'),
        ];
    }
}
```

### Registering the Resource in a Panel

If the project uses a single panel, register in `app/Providers/Filament/{Panel}ServiceProvider.php`.

If multi-panel or module-scoped, create a plugin:

```php
// Modules/{Name}/app/Providers/Filament/{Name}Plugin.php
use Filament\Contracts\Plugin;
use Filament\Panel;

class {Name}Plugin implements Plugin
{
    public function getId(): string { return '{name}'; }

    public function register(Panel $panel): void
    {
        $panel->resources([
            \Modules\{Name}\App\Filament\Resources\{Model}Resource::class,
        ]);
    }

    public function boot(Panel $panel): void {}

    public static function make(): static
    {
        return app(static::class);
    }
}
```

Then in `PanelServiceProvider`:

```php
->plugins([
    \Modules\{Name}\App\Providers\Filament\{Name}Plugin::make(),
])
```

---

## 5. Filament Forms & Tables

### Forms — Common Components

```php
use Filament\Forms\Components\{TextInput, Textarea, Select, Toggle,
    DatePicker, FileUpload, Repeater, Section, Grid};

// Bilingual text field (ar + en tabs)
use Filament\Forms\Components\Tabs;

Tabs::make('Translations')
    ->tabs([
        Tabs\Tab::make('English')->schema([
            TextInput::make('name.en')
                ->label('Name (English)')
                ->required(),
        ]),
        Tabs\Tab::make('Arabic')->schema([
            TextInput::make('name.ar')
                ->label('الاسم (عربي)')
                ->required()
                ->dir('rtl'),
        ]),
    ]),

// Other common fields
Select::make('category_id')
    ->label(__('module.category'))
    ->relationship('category', 'name')
    ->searchable()
    ->preload()
    ->required(),

Toggle::make('is_active')
    ->label(__('module.is_active'))
    ->default(true),

FileUpload::make('image')
    ->label(__('module.image'))
    ->image()
    ->directory('uploads/{module}'),
```

### Tables — Common Columns & Filters

```php
use Filament\Tables\Columns\{TextColumn, IconColumn, ImageColumn, BadgeColumn};
use Filament\Tables\Filters\{SelectFilter, TernaryFilter};
use Filament\Tables\Actions\{EditAction, DeleteAction, BulkActionGroup, DeleteBulkAction};

// Columns
TextColumn::make('name')          // if json: cast/accessor needed
    ->label(__('module.name'))
    ->searchable()
    ->sortable(),

IconColumn::make('is_active')
    ->label(__('module.is_active'))
    ->boolean(),

TextColumn::make('created_at')
    ->label(__('module.created_at'))
    ->dateTime()
    ->sortable()
    ->toggleable(isToggledHiddenByDefault: true),

// Filters
TernaryFilter::make('is_active')
    ->label(__('module.is_active')),

SelectFilter::make('category_id')
    ->label(__('module.category'))
    ->relationship('category', 'name'),

// Actions
->actions([EditAction::make(), DeleteAction::make()])
->bulkActions([BulkActionGroup::make([DeleteBulkAction::make()])])
```

---

## 6. Translations (ar / en)

### File structure

```php
// Modules/{Name}/lang/en/{module}.php
return [
    'singular'    => 'Product',
    'plural'      => 'Products',
    'name'        => 'Name',
    'description' => 'Description',
    'category'    => 'Category',
    'is_active'   => 'Active',
    'created_at'  => 'Created At',
];

// Modules/{Name}/lang/ar/{module}.php
return [
    'singular'    => 'منتج',
    'plural'      => 'المنتجات',
    'name'        => 'الاسم',
    'description' => 'الوصف',
    'category'    => 'الفئة',
    'is_active'   => 'مفعّل',
    'created_at'  => 'تاريخ الإنشاء',
];
```

### Usage in code

```php
__('module-name::module.plural')
// or via helper if custom:
trans('module-name::module.name')
```

### Loading lang from module

In the module's `ServiceProvider`:

```php
public function boot(): void
{
    $this->loadTranslationsFrom(module_path('{Name}', 'lang'), '{name}');
}
```

---

## 7. Quick Reference — Common Artisan Commands

```bash
# Module scaffolding
php artisan module:make {Name}
php artisan module:make-model {Model} {Name}
php artisan module:make-migration create_{table}_table {Name}
php artisan module:make-seeder {Name}Seeder {Name}
php artisan module:make-controller {Name}Controller {Name}
php artisan module:make-request Store{Name}Request {Name}
php artisan module:make-service {Name}Service {Name}

# Factory (manual — nWidart may not have a make:factory command)
# Create: Modules/{Name}/database/factories/{Model}Factory.php

# Migrations
php artisan module:migrate {Name}
php artisan module:migrate-rollback {Name}
php artisan module:seed {Name}

# Tests
php artisan make:test Modules/{Name}/tests/Feature/{Endpoint}Test
php artisan make:test Modules/{Name}/tests/Unit/{Service}Test --unit
php artisan test --filter {TestName}

# Filament
php artisan make:filament-resource {Model} --module={Name}  # if supported
php artisan make:filament-page {Page} --panel={panel}
```

---

## 8. Conventions & Rules

| Rule                 | Detail                                                    |
| -------------------- | --------------------------------------------------------- |
| Namespace            | `Modules\{Name}\App\...`                                  |
| Route prefix         | `/api/v1/{module}/` for API, `/{module}/` for web         |
| Translatable columns | Store as `json`, use accessor or spatie/translatable      |
| Filament labels      | Always use `__()` — never hardcode English/Arabic strings |
| Form RTL fields      | Add `->dir('rtl')` on Arabic text inputs                  |
| Soft deletes         | Use by default on main entities                           |
| Active scope         | Add `scopeActive($q)` on every main model                 |

---

## 9. Read Reference Files When Needed

- `references/filament-advanced.md` — Custom pages, Widgets, Actions, Notifications
- `references/module-relations.md` — Cross-module relations & service patterns
- `references/translation-patterns.md` — Spatie translatable deep dive

> Read these only when the task requires it — don't load all of them upfront.
