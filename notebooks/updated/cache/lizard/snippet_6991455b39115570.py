def get_new(self):
    self.refresh()
    new_info = self._load()
    old_info = self._load(prev_version=True)
    new_files = new_info[-new_info.isin(old_info)]
    return new_files