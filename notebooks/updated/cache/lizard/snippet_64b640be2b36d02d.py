def parse(cls, string):
    obj, i = cls.match(string, 0)
    if i != len(string):
        raise Exception("Could not parse '" + string + "' beyond index " +
            str(i))
    return obj