def rename(self, new_name):
    if self.name == new_name:
        return self
    self.repo.git.remote('rename', self.name, new_name)
    self.name = new_name
    self._clear_cache()
    return self