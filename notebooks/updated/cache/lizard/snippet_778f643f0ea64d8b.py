def MoveToAttributeNo(self, no):
    ret = libxml2mod.xmlTextReaderMoveToAttributeNo(self._o, no)
    return ret