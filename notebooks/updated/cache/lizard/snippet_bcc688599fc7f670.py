def show_tree(self):
    self.initialize_view()
    self.setItemsExpandable(True)
    self.setSortingEnabled(False)
    rootkey = self.find_root()
    if rootkey:
        self.populate_tree(self, self.find_callees(rootkey))
        self.resizeColumnToContents(0)
        self.setSortingEnabled(True)
        self.sortItems(1, Qt.AscendingOrder)
        self.change_view(1)