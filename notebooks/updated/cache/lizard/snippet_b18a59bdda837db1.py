def is_file(self, follow_symlinks=True):
    return self._system.isfile(path=self._path, client_kwargs=self.
        _client_kwargs)