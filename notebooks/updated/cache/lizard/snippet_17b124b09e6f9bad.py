def close_temp_file(self):
    self.temporary_file.close()
    if self._orig_file is not None:
        self._orig_file.close()