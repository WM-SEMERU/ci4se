def attribute(func):

    def inner(self):
        name, attribute_type = func(self)
        if not name:
            name = func.__name__
        try:
            return attribute_type(self.et.attrib[name])
        except KeyError:
            raise AttributeError
    return inner