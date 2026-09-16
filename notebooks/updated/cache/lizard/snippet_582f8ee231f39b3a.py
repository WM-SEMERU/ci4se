def save_attr(self, entity, value):
    if self.datatype == self.TYPE_MANY:
        self._save_m2m_attr(entity, value)
    else:
        self._save_single_attr(entity, value)