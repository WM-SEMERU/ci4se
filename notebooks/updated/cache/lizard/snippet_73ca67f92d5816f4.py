def delete(self, where=None, start=None, stop=None, **kwargs):
    if com._all_none(where, start, stop):
        self._handle.remove_node(self.group, recursive=True)
        return None
    raise TypeError('cannot delete on an abstract storer')