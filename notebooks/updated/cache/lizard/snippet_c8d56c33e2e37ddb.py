def remove_private_obfuscation(self):
    classname = self.__class__.__name__
    attrlist = [attr for attr in dir(self) if attr.startswith('_' +
        classname + '__')]
    for attr in attrlist:
        method = getattr(self, attr)
        truename = attr.replace('_' + classname + '__', '__')
        setattr(self, truename, method)