def set_autoreload_params(self, scan_interval=None, ignore_modules=None):
    self._set('py-auto-reload', scan_interval)
    self._set('py-auto-reload-ignore', ignore_modules, multi=True)
    return self._section