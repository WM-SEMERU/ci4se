def is_running(self):
    if self._postmaster_proc:
        if self._postmaster_proc.is_running():
            return self._postmaster_proc
        self._postmaster_proc = None
    self._schedule_load_slots = self.use_slots
    self._postmaster_proc = PostmasterProcess.from_pidfile(self._data_dir)
    return self._postmaster_proc