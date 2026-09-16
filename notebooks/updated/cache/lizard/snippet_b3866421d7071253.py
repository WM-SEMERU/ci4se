def get_id(self):
    if self._id_attr is None or not hasattr(self, self._id_attr):
        return None
    return getattr(self, self._id_attr)