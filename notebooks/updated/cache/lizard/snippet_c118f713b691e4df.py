def filter_by(cls, **kwargs):
    limit = kwargs.pop('limit', None)
    reverse = kwargs.pop('reverse', False)
    q = cls.query.filter_by(**kwargs)
    if reverse:
        q = q.order_by(cls.id.desc())
    if limit:
        q = q.limit(limit)
    return q