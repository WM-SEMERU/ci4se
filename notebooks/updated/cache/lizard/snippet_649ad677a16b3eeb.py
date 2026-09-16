def get_object(self, view_kwargs, qs=None):
    self.before_get_object(view_kwargs)
    id_field = getattr(self, 'id_field', inspect(self.model).primary_key[0].key
        )
    try:
        filter_field = getattr(self.model, id_field)
    except Exception:
        raise Exception('{} has no attribute {}'.format(self.model.__name__,
            id_field))
    url_field = getattr(self, 'url_field', 'id')
    filter_value = view_kwargs[url_field]
    query = self.retrieve_object_query(view_kwargs, filter_field, filter_value)
    if qs is not None:
        query = self.eagerload_includes(query, qs)
    try:
        obj = query.one()
    except NoResultFound:
        obj = None
    self.after_get_object(obj, view_kwargs)
    return obj