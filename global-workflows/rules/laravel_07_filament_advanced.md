---
trigger: model_decision
description: "Laravel HMVC Clean Architecture Rule: 07_filament_advanced.md"
---

# Filament Advanced Patterns

## Custom Standalone Pages (inside module)

```php
// Modules/{Name}/app/Filament/Pages/Dashboard.php
namespace Modules\{Name}\App\Filament\Pages;

use Filament\Pages\Page;

class Dashboard extends Page
{
    protected static ?string $navigationIcon = 'heroicon-o-home';
    protected static string $view = 'module-name::filament.pages.dashboard';

    public static function getNavigationLabel(): string
    {
        return __('module-name::module.dashboard');
    }
}
```

## Widgets

```php
// StatsOverviewWidget
use Filament\Widgets\StatsOverviewWidget as BaseWidget;
use Filament\Widgets\StatsOverviewWidget\Stat;

class StatsOverview extends BaseWidget
{
    protected function getStats(): array
    {
        return [
            Stat::make(__('module.total_orders'), Order::count())
                ->description(__('module.all_time'))
                ->color('success'),
        ];
    }
}
```

Register widget in plugin or panel:

```php
$panel->widgets([
    \Modules\{Name}\App\Filament\Widgets\StatsOverview::class,
]);
```

## Custom Table Actions

```php
use Filament\Tables\Actions\Action;

Action::make('approve')
    ->label(__('module.approve'))
    ->icon('heroicon-o-check')
    ->color('success')
    ->requiresConfirmation()
    ->action(function ($record) {
        $record->update(['status' => 'approved']);
        Notification::make()->title(__('module.approved'))->success()->send();
    })
    ->visible(fn($record) => $record->status === 'pending'),
```

## Notifications

```php
use Filament\Notifications\Notification;

Notification::make()
    ->title(__('module.saved_successfully'))
    ->success()
    ->send();

// With body
Notification::make()
    ->title(__('module.error'))
    ->body(__('module.something_went_wrong'))
    ->danger()
    ->send();
```

## Form Hooks (on create/edit pages)

```php
// In Create{Model}.php page
protected function mutateFormDataBeforeCreate(array $data): array
{
    $data['user_id'] = auth()->id();
    return $data;
}

// In Edit{Model}.php page
protected function mutateFormDataBeforeSave(array $data): array
{
    // transform before save
    return $data;
}
```

## Relation Managers

```php
// Modules/{Name}/app/Filament/Resources/{Model}Resource/RelationManagers/ItemsRelationManager.php
use Filament\Resources\RelationManagers\RelationManager;

class ItemsRelationManager extends RelationManager
{
    protected static string $relationship = 'items';

    public function form(Form $form): Form
    {
        return $form->schema([
            TextInput::make('name')->required(),
        ]);
    }

    public function table(Table $table): Table
    {
        return $table->columns([
            TextColumn::make('name'),
        ]);
    }
}

// Register in resource:
public static function getRelations(): array
{
    return [
        ItemsRelationManager::class,
    ];
}
```

## Navigation Groups & Sorting

```php
class {Model}Resource extends Resource
{
    protected static ?string $navigationGroup = null; // set dynamically

    public static function getNavigationGroup(): ?string
    {
        return __('module-name::module.nav_group');
    }

    protected static ?int $navigationSort = 1;
}
```

## Global Search

```php
class {Model}Resource extends Resource
{
    protected static ?string $recordTitleAttribute = 'name';

        return [
            __('module.category') => $record->category?->name,
        ];
    }
}
```

## Navigation Groups & Icons

Standardize the sidebar organization:
- Use consistent navigation groups using translations: `__('core::nav.settings')`, `__('user-management::nav.users')`, etc.
- Use **Heroicons** v2.
- Sort related resources using `navigationSort` to keep the menu logical.

## Bilingual Support in Filament (best practices)

- **Input Separation**: Always use `Tabs` or `Section` to separate Arabic and English inputs.
- **RTL Context**: Use `->dir('rtl')` for all Arabic inputs to ensure correct rendering.
- **Labels**: Labels must ALWAYS use `__()` with module-namespaced keys: `__('module::file.key')`.

```php
Tabs::make('Translations')
    ->tabs([
        Tabs\Tab::make('English')->schema([
            TextInput::make('name.en')
                ->label(__('module::file.name_en'))
                ->required(),
        ]),
        Tabs\Tab::make('Arabic')->schema([
            TextInput::make('name.ar')
                ->label(__('module::file.name_ar'))
                ->required()
                ->dir('rtl'),
        ]),
    ])
```

- **Table Columns**: For translatable JSON columns, use an accessor or dot notation if using `spatie/translatable`.
  ```php
  TextColumn::make('name.' . app()->getLocale())
      ->label(__('module::file.name'))
      ->searchable()
  ```
