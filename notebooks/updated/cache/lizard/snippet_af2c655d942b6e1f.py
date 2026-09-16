def run(self):
    query = self.query
    self.cardinality = query.add_columns(self.columns[0].sqla_expr).count()
    self._set_column_filter_expressions()
    self._set_global_filter_expression()
    self._set_sort_expressions()
    self._set_yadcf_data(query)
    query = query.filter(*[e for e in self.filter_expressions if e is not None]
        )
    self.cardinality_filtered = query.add_columns(self.columns[0].sqla_expr
        ).count()
    query = query.order_by(*[e for e in self.sort_expressions if e is not None]
        )
    length = int(self.params.get('length'))
    if length >= 0:
        query = query.limit(length)
    elif length == -1:
        pass
    else:
        raise ValueError('Length should be a positive integer or -1 to disable'
            )
    query = query.offset(int(self.params.get('start')))
    query = query.add_columns(*[c.sqla_expr for c in self.columns])
    column_names = [(col.mData if col.mData else str(i)) for i, col in
        enumerate(self.columns)]
    self.results = [{k: v for k, v in zip(column_names, row)} for row in
        query.all()]