def clean_cache(self, section=None):
    self.remove_all_locks()
    if section is not None and '/' in section:
        raise ValueError("invalid section '{0}'".format(section))
    if section is not None:
        path = os.path.join(self._full_base, section)
    else:
        path = self._full_base
    if not os.path.exists(path):
        return
    shutil.rmtree(path)