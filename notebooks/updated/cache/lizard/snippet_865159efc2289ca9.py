def getCursor(self):
    if self.connection is None:
        self.Connect()
    return self.connection.cursor(MySQLdb.cursors.DictCursor)