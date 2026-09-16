def link(self, source_key, target_key):
    link_value = self._link_value_for_key(source_key)
    self.child_datastore.put(target_key, link_value)
    self.get(target_key)