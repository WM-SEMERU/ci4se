def create_mysql_cymysql(self, **kwargs):
    return self._ce(self._ccs(self.DialectAndDriver.mysql_cymysql), **kwargs)