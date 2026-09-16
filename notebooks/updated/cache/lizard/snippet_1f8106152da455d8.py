def all(self, query=None):
    if query is None:
        query = {}
    if self.content_type_id is not None:
        query['content_type'] = self.content_type_id
    normalize_select(query)
    return super(EntriesProxy, self).all(query=query)