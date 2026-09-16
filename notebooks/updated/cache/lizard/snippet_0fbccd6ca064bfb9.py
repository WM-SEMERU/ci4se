def get_one(self, schema, query=None, **kwargs):
    ret = self._get_query(self._get_one, schema, query, **kwargs)
    if not ret:
        ret = {}
    return ret