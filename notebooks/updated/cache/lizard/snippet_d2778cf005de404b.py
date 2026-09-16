def parse(fileobject, schema=None):
    if schema:
        parser = objectify.makeparser(schema=schema.schema, strip_cdata=False)
        return objectify.parse(fileobject, parser=parser)
    else:
        return objectify.parse(fileobject)