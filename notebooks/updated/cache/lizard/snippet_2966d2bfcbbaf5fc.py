def protocol(self, name):
    return self.query(Protocol).filter(Protocol.name == name).one()