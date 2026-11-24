---
trigger: model_decision
description: "Flutter Architecture Rule: 10_pagination_standard.md"
---

# 10. Pagination Standard (The Gold Standard)

This document defines the mandatory pattern for implementing infinite scrolling (Pagination). **NEVER** deviate from this pattern.

---

## 1. Architecture Layers

### Domain Layer (Entities)
- **`Paginate`**: (from `core/pagination/paginate_entity.dart`).
- **`PaginatedResult<T>`**: Wrapper for results and metadata.

### Data Layer (Mappers)
- **Mapper**: Use `.toPaginatedResult()` extension on DTO lists.
```dart
Future<PaginatedResult<MyEntity>> getItems(int page) async {
  final response = await _dataSource.getItems(page);
  return response.toPaginatedResult<MyEntity>((dto) => dto.toEntity());
}
```

### Logic Layer (Cubit Mixing)
- **Mixin**: `with PaginationMixin<TState, TItem>`.
- **Mandatory**: Call `initPagination()` in constructor and `disposePagination()` in `close()`.
```dart
class MyCubit extends Cubit<MyState> with PaginationMixin<MyState, MyEntity> {
  MyCubit(this._useCase) : super(MyState()) { initPagination(); }

  @override
  Future<PaginatedResult<MyEntity>> fetchPage(int page) => _useCase(page);

  @override
  void getItems({int page = 1, bool showLoading = true}) => loadPage(page: page, showLoading: showLoading);
}
```

---

## 2. UI Layer (`StatesScreenList/Grid`)
Connect the logic to the UI using the `PaginationController`.

```dart
StatesScreenList<MyEntity>(
  status: state.getStatus,
  paginationController: cubit.paginationController, // MANDATORY
  onRetry: () => cubit.getItems(showLoading: false),
  itemBuilder: (context, item, index) => MyItemWidget(item: item),
  loadingItems: MyEntity.fakeList(),
  loadingWidget: (context, item, index) => MyLoadingWidget(),
)
```

---

## 3. Summary of Responsibilities
1. **`PaginationController`**: Manages the `ScrollController`, current page, and `isLoadingMore` flag.
2. **`PaginationMixin`**: Handles the `loadPage` logic and item appending.
3. **`StatesScreenList`**: Listens to the controller to render the loading footer automatically.
