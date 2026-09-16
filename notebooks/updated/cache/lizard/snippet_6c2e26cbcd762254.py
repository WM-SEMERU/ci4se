def _rewrite_applied_operations(self):
    self._rewrite_where(self.query.where)
    self._rewrite_order()
    self._rewrite_select_related()