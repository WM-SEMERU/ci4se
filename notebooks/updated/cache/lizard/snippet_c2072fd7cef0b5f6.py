def xincludeProcessFlags(self, flags):
    ret = libxml2mod.xmlXIncludeProcessFlags(self._o, flags)
    return ret