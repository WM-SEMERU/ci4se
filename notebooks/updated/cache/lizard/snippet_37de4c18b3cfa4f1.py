def Connect(self):
    if self.connection is None:
        self.connection = MySQLdb.connect(*[], **self.connectionInfo.info)
    if self.connectionInfo.commitOnEnd is True:
        self.connection.autocommit()
    self._updateCheckTime()