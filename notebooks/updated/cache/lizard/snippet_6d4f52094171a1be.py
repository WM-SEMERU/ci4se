def _local_update(self, rdict):
    sanitized = self._check_keys(rdict)
    temp_meta = self._meta_data
    self.__dict__ = sanitized
    self._meta_data = temp_meta