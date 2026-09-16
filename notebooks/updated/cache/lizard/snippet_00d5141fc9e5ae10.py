def getSchema(cls):
    schema = []
    for name, atr in cls.__attributes__:
        atr = atr.__get__(None, cls)
        if isinstance(atr, SQLAttribute):
            schema.append((name, atr))
    cls.getSchema = staticmethod(lambda schema=schema: schema)
    return schema