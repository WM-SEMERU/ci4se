def dropDataProducts(self, *pathnames):
    trash = QTreeWidget(None)
    updated = False
    for path in pathnames:
        item = self.dpitems.get(path)
        if item and not item._dp.archived:
            self.takeTopLevelItem(self.indexOfTopLevelItem(item))
            trash.addTopLevelItem(item)
            del self.dpitems[path]
            updated = True
    if updated:
        self.emit(SIGNAL('updated'))