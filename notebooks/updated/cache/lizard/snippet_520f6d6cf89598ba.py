def qualified_name(self):
    o = VersionedObject.construct(self.name, self.version)
    return str(o)