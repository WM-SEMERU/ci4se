def getPaintItems(self, root=None):
    if root is None:
        root = self.item
    preItems = []
    postItems = []
    if isinstance(root, QtGui.QGraphicsScene):
        childs = [i for i in root.items() if i.parentItem() is None]
        rootItem = []
    else:
        try:
            childs = root.childItems()
        except:
            childs = root.items()
        rootItem = [root]
    childs.sort(key=lambda a: a.zValue())
    while len(childs) > 0:
        ch = childs.pop(0)
        tree = self.getPaintItems(ch)
        if int(ch.flags() & ch.ItemStacksBehindParent) > 0 or ch.zValue(
            ) < 0 and int(ch.flags() & ch.ItemNegativeZStacksBehindParent) > 0:
            preItems.extend(tree)
        else:
            postItems.extend(tree)
    return preItems + rootItem + postItems