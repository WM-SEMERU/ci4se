def printSkosTree(self, element=None, showids=False, labels=False, showtype
    =False):
    TYPE_MARGIN = 13
    if not element:
        for x in self.toplayerSkosConcepts:
            printGenericTree(x, 0, showids, labels, showtype, TYPE_MARGIN)
    else:
        printGenericTree(element, 0, showids, labels, showtype, TYPE_MARGIN)