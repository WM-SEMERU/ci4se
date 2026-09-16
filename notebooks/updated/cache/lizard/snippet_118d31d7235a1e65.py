def isConnected(self, fromName, toName):
    for c in self.connections:
        if c.fromLayer.name == fromName and c.toLayer.name == toName:
            return 1
    return 0