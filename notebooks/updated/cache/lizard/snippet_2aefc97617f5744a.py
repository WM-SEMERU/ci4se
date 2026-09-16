def set_file_params(self, reopen_on_reload=None, trucate_on_statup=None,
    max_size=None, rotation_fname=None, touch_reopen=None, touch_rotate=
    None, owner=None, mode=None):
    self._set('log-reopen', reopen_on_reload, cast=bool)
    self._set('log-truncate', trucate_on_statup, cast=bool)
    self._set('log-maxsize', max_size)
    self._set('log-backupname', rotation_fname)
    self._set('touch-logreopen', touch_reopen, multi=True)
    self._set('touch-logrotate', touch_rotate, multi=True)
    self._set('logfile-chown', owner)
    self._set('logfile-chmod', mode)
    return self._section