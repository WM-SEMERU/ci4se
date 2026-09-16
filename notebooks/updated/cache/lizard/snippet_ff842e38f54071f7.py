def open(self):
    if self._rpc is not None:
        return self._rpc
    self.load_config()
    if not config.scgi_url:
        raise error.UserError(
            'You need to configure a XMLRPC connection, read https://pyrocore.readthedocs.io/en/latest/setup.html'
            )
    self._rpc = xmlrpc.RTorrentProxy(config.scgi_url)
    self.versions, self.version_info = self._rpc._set_mappings()
    self.engine_id = self._rpc.session.name()
    time_usec = self._rpc.system.time_usec()
    if time_usec < 2 ** 32:
        self.LOG.warn(
            'Your xmlrpc-c is broken (64 bit integer support missing, %r returned instead)'
             % (type(time_usec),))
    self.engine_software = 'rTorrent %s/%s' % self.versions
    if '+ssh:' in config.scgi_url:
        self.startup = int(self._rpc.startup_time() or time.time())
    else:
        self._session_dir = self._rpc.session.path()
        if not self._session_dir:
            raise error.UserError(
                'You need a session directory, read https://pyrocore.readthedocs.io/en/latest/setup.html'
                )
        if not os.path.exists(self._session_dir):
            raise error.UserError('Non-existing session directory %r' %
                self._session_dir)
        self._download_dir = os.path.expanduser(self._rpc.directory.default())
        if not os.path.exists(self._download_dir):
            raise error.UserError('Non-existing download directory %r' %
                self._download_dir)
        self.startup = os.path.getmtime(os.path.join(self._session_dir,
            'rtorrent.lock'))
    self.LOG.debug(repr(self))
    return self._rpc