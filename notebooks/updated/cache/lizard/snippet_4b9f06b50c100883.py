def _load_data(self, data, from_db=False):
    self._data = data[:]
    self.setattrs(values=[], node_stack=[], node_dict={})
    self._from_db = from_db