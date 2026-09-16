def paginate(self, per_page=None, current_page=None, columns=None):
    if columns is None:
        columns = ['*']
    total = self.to_base().get_count_for_pagination()
    page = current_page or Paginator.resolve_current_page()
    per_page = per_page or self._model.get_per_page()
    self._query.for_page(page, per_page)
    return LengthAwarePaginator(self.get(columns).all(), total, per_page, page)