def createTable(self, login, tableName, versioningIter, type):
    self.send_createTable(login, tableName, versioningIter, type)
    self.recv_createTable()