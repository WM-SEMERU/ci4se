def get_path(self, wd):
    watch_ = self._wmd.get(wd)
    if watch_ is not None:
        return watch_.path