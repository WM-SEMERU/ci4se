def constants(self):
    ret = {}
    name = self.__class_name.split('.')[-1]
    constant_class = getattr(self.__module, name)
    for name, value in constant_class.__dict__.items():
        if re.match('^[A-Z][A-Z0-9_]*$', name):
            ret[name] = value
    return ret