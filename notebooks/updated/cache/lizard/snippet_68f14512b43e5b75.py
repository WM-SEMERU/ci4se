def setProperty(self, login, property, value):
    self.send_setProperty(login, property, value)
    self.recv_setProperty()