def _query_select_options(self, query, select_columns=None):
    if select_columns:
        _load_options = list()
        for column in select_columns:
            if '.' in column:
                model_relation = self.get_related_model(column.split('.')[0])
                if not self.is_model_already_joinded(query, model_relation):
                    query = query.join(model_relation)
                _load_options.append(Load(model_relation).load_only(column.
                    split('.')[1]))
            elif not self.is_relation(column) and not hasattr(getattr(self.
                obj, column), '__call__'):
                _load_options.append(Load(self.obj).load_only(column))
            else:
                _load_options.append(Load(self.obj))
        query = query.options(*tuple(_load_options))
    return query