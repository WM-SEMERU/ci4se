def addMenuItem(self, newItem, atItem):
    tree = self.uiMenuTREE
    if not atItem:
        tree.addTopLevelItem(newItem)
    elif atItem.data(0, Qt.UserRole) == 'menu':
        atItem.addChild(newItem)
    elif atItem.parent():
        index = atItem.parent().indexOfChild(atItem)
        atItem.parent().insertChild(index + 1, newItem)
    else:
        index = tree.indexOfTopLevelItem(atItem)
        tree.insertTopLevelItem(index + 1, newItem)