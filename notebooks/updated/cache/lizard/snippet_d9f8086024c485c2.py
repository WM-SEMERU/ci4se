def prop(self, name):
    ret = libxml2mod.xmlGetProp(self._o, name)
    return ret