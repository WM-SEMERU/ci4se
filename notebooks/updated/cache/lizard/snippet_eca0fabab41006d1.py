def save_module(self, path, module, change_time=None):
    if settings.use_filesystem_cache == False:
        return
    self.__index = None
    try:
        files = self._index
    except KeyError:
        files = {}
        self._index = files
    target_path = self._get_hashed_path(path)
    with open(target_path, 'wb') as f:
        pickle.dump(module, f, pickle.HIGHEST_PROTOCOL)
        if change_time is None:
            files[path] = module[0].change_time
        else:
            files[path] = change_time
    self._flush_index()