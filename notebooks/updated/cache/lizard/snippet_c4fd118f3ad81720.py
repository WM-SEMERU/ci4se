def _on_delete(self, builder):
    column = self._get_deleted_at_column(builder)
    return builder.update({column: builder.get_model().fresh_timestamp()})