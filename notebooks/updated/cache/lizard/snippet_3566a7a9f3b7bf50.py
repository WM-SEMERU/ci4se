def dict_has_all_keys(self, keys):
    if not _is_non_string_iterable(keys):
        keys = [keys]
    with cython_context():
        return SArray(_proxy=self.__proxy__.dict_has_all_keys(keys))