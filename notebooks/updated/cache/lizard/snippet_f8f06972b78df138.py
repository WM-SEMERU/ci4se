def sendPassword(self, password):
    pw = (password + '\x00' * 8)[:8]
    des = RFBDes(pw)
    response = des.encrypt(self._challenge)
    self.transport.write(response)