def from_schemafile(cls, schemafile):
    with open(schemafile) as f:
        return cls(json.load(f))