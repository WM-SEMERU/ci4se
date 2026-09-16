def groupQuery(self):
    items = self.uiQueryTREE.selectedItems()
    if not len(items) > 2:
        return
    if isinstance(items[-1], XJoinItem):
        items = items[:-1]
    tree = self.uiQueryTREE
    parent = items[0].parent()
    if not parent:
        parent = tree
    preceeding = items[-1]
    tree.blockSignals(True)
    tree.setUpdatesEnabled(False)
    grp_item = XQueryItem(parent, Q(), preceeding=preceeding)
    for item in items:
        parent = item.parent()
        if not parent:
            tree.takeTopLevelItem(tree.indexOfTopLevelItem(item))
        else:
            parent.takeChild(parent.indexOfChild(item))
        grp_item.addChild(item)
    grp_item.update()
    tree.blockSignals(False)
    tree.setUpdatesEnabled(True)