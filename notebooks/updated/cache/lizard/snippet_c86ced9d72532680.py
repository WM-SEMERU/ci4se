def add_watched_directory(self, dir_path):
    req = ApiWatchedDir(self._get_resource_root(), path=dir_path)
    return self._post('watcheddir', ApiWatchedDir, data=req, api_version=14)