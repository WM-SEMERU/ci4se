def from_config(cls, pyvlx, item):
    name = item['name']
    ident = item['id']
    return cls(pyvlx, ident, name)