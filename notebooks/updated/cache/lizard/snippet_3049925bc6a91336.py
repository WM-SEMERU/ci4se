def nodeListGetString(self, list, inLine):
    if list is None:
        list__o = None
    else:
        list__o = list._o
    ret = libxml2mod.xmlNodeListGetString(self._o, list__o, inLine)
    return ret