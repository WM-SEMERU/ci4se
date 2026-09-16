def _select_query(self):
    if self._where:
        self._validate_select_where()
    return SelectStatement(self.column_family_name, fields=self.
        _select_fields(), where=self._where, order_by=self._order, limit=
        self._limit, allow_filtering=self._allow_filtering, distinct_fields
        =self._distinct_fields, fetch_size=self._fetch_size)