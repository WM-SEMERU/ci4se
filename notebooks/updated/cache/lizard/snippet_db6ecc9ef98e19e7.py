def setLocalityGroups(self, login, tableName, groups):
    self.send_setLocalityGroups(login, tableName, groups)
    self.recv_setLocalityGroups()