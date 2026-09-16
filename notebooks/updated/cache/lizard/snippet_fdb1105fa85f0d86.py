def find_many(self, id, columns=None):
    if columns is None:
        columns = ['*']
    if not id:
        return self._model.new_collection()
    self._query.where_in(self._model.get_qualified_key_name(), id)
    return self.get(columns)