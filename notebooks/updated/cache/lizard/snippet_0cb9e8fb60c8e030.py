def query_model(self, model, condition=None, offset=None, limit=None,
    group_by=None, having=None, order_by=None, fields=None):
    if self._query is not None:
        query = self._query
    else:
        query = self.get_select()
    if condition is not None:
        if isinstance(query, Result):
            query = query.filter(condition)
        else:
            query = query.where(condition)
    if self.pagination:
        if offset is not None:
            query = query.offset(int(offset))
        if limit is not None:
            query = query.limit(int(limit))
    if order_by is not None:
        if isinstance(order_by, (tuple, list)):
            for order in order_by:
                query = query.order_by(order)
        else:
            query = query.order_by(order_by)
    if group_by is not None:
        if isinstance(group_by, (tuple, list)):
            query = query.group_by(*group_by)
        else:
            query = query.group_by(group_by)
        if having is not None:
            query = query.having(having)
    return query