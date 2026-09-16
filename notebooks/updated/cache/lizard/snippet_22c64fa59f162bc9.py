def add(self, schema):
    key = schema.tns[1]
    existing = self.namespaces.get(key)
    if existing is None:
        self.children.append(schema)
        self.namespaces[key] = schema
    else:
        existing.root.children += schema.root.children
        existing.root.nsprefixes.update(schema.root.nsprefixes)