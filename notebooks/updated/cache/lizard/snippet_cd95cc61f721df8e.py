def read_file(self):
    if not self._cfg_path:
        return
    try:
        cfg_fp = open(self._cfg_path, 'r')
        self.readfp(cfg_fp)
    except IOError as exc:
        raise NipapConfigError(str(exc))