def textConcat(self, content, len):
    ret = libxml2mod.xmlTextConcat(self._o, content, len)
    return ret