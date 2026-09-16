def _get_writable_cache_dir(self):
    dir_path_data = self._get_default_cache_dir()
    if os.access(dir_path_data, os.W_OK):
        self._default_cache_file = True
        return dir_path_data
    dir_path_user = user_cache_dir(self._URLEXTRACT_NAME)
    if not os.path.exists(dir_path_user):
        os.makedirs(dir_path_user, exist_ok=True)
    if os.access(dir_path_user, os.W_OK):
        return dir_path_user
    dir_path_temp = tempfile.gettempdir()
    if os.access(dir_path_temp, os.W_OK):
        return dir_path_temp
    raise CacheFileError('Cache directories are not writable.')