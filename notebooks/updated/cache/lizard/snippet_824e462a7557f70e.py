def _start(self):
    assert self._tempdir is not None
    assert self._process is None
    self._process = subprocess.Popen([self.paths.slapd, '-f', self.
        _slapd_conf, '-h', self.uri, '-d', str(self.slapd_debug)], stdout=
        sys.stdout, stderr=sys.stderr)
    self._poll_slapd(timeout=self.max_server_startup_delay)