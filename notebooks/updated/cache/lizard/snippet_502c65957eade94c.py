def import_schema(self, definitions, d):
    if not len(definitions.types):
        types = Types.create(definitions)
        definitions.types.append(types)
    else:
        types = definitions.types[-1]
    types.root.append(d.root)
    log.debug('imported (XSD):\n%s', d.root)