def fromElement(cls, elem):
    self = cls()
    self.oid = elem.get('OID')
    self.name = elem.get('Name')
    return self