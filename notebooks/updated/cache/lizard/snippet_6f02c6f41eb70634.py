def _make_lock_path(self, lock_name_base):
    base, name = os.path.split(lock_name_base)
    lock_name = self._ensure_lock_prefix(name)
    if base:
        lock_name = os.path.join(base, lock_name)
    return pipeline_filepath(self, filename=lock_name)