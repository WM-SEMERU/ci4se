def convert_to_ip(self):
    if not self.is_data_loaded:
        self._import_data()
    if self.is_ip is False:
        for coll in self._data:
            coll.convert_to_ip()
    self._is_ip = True