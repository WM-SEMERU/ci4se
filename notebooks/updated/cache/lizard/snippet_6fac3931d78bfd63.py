def receiveError(self, reasonCode, description):
    error = disconnectErrors.get(reasonCode, DisconnectError)
    self.connectionClosed(error(reasonCode, description))
    SSHClientTransport.receiveError(self, reasonCode, description)