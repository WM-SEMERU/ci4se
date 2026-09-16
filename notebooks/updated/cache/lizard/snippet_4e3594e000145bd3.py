def save_to_store(self):
    if not self._store:
        raise AttributeError('No datastore defined!')
    saved_data = self.save_to_data(in_place=True)
    data = Serializer.serialize(saved_data)
    self._store.store_blob(data, 'all_keys_with_undefined')