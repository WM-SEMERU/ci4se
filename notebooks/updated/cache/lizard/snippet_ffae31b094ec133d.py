def save(self):
    pk_field = self._fields[self._primary_key]
    if not self._data.get(self._primary_key):
        setattr(self, self._primary_key, pk_field._generate_key())
        require_delete = False
    else:
        require_delete = True
    if require_delete:
        self.delete(for_update=True)
    data = self._get_data_dict()
    hash_obj = self.to_hash()
    hash_obj.clear()
    hash_obj.update(data)
    all_index = self._query.all_index()
    all_index.add(self.get_hash_id())
    for field in self._indexes:
        for index in field.get_indexes():
            index.save(self)