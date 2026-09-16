def retrieveVals(self):
    fpminfo = PHPfpmInfo(self._host, self._port, self._user, self._password,
        self._monpath, self._ssl)
    stats = fpminfo.getStats()
    if self.hasGraph('php_fpm_connections') and stats:
        self.setGraphVal('php_fpm_connections', 'conn', stats['accepted conn'])
    if self.hasGraph('php_fpm_processes') and stats:
        self.setGraphVal('php_fpm_processes', 'active', stats[
            'active processes'])
        self.setGraphVal('php_fpm_processes', 'idle', stats['idle processes'])
        self.setGraphVal('php_fpm_processes', 'total', stats['total processes']
            )