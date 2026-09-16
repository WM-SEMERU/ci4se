def getActiveCompactions(self, login, tserver):
    self.send_getActiveCompactions(login, tserver)
    return self.recv_getActiveCompactions()