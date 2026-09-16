def _DetermineFormat(self):
    if self._zip:
        assert not self._path
        return True
    if not isinstance(self._path, basestring) and hasattr(self._path, 'read'):
        self._zip = zipfile.ZipFile(self._path, mode='r')
        return True
    if not os.path.exists(self._path):
        self._problems.FeedNotFound(self._path)
        return False
    if self._path.endswith('.zip'):
        try:
            self._zip = zipfile.ZipFile(self._path, mode='r')
        except IOError:
            pass
        except zipfile.BadZipfile:
            self._problems.UnknownFormat(self._path)
            return False
    if not self._zip and not os.path.isdir(self._path):
        self._problems.UnknownFormat(self._path)
        return False
    return True