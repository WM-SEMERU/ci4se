def send(self, message):
    for transport in self.transports.values():
        transport.protocol.sendMessage(message)