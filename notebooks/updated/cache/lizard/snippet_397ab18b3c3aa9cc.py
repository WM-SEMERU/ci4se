def printPropertyTree(self, element=None, showids=False, labels=False,
    showtype=False):
    TYPE_MARGIN = 18
    if not element:
        for x in self.toplayer_properties:
            printGenericTree(x, 0, showids, labels, showtype, TYPE_MARGIN)
    else:
        printGenericTree(element, 0, showids, labels, showtype, TYPE_MARGIN)