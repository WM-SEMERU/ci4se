def publictypes(self):
    for t in self.wsdl.schema.types.values():
        if t in self.params:
            continue
        if t in self.types:
            continue
        item = t, t
        self.types.append(item)
    self.types.sort(key=lambda x: x[0].name)