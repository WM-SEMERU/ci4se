def sidpath(self, sid):
    sid_subdir = _sid_subdir_path(sid)
    return join(self._rootdir, sid_subdir)