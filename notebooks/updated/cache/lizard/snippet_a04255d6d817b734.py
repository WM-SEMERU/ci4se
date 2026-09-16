def get(self, po):
    name = po.name
    typ = po.typ
    default = po.default
    handler = getattr(self, '_get_{}'.format(typ), None)
    if handler is None:
        raise ValueError(typ)
    self.seen.add(name)
    if not self.parser.has_option(self.section, name):
        if default is REQUIRED:
            raise NameError(self.section, name)
        if isinstance(default, INHERIT_GLOBAL):
            return handler('global', name, default.default)
    return handler(self.section, name, default)