def initializePage(self):
    tree = self.uiStructureTREE
    tree.blockSignals(True)
    tree.setUpdatesEnabled(False)
    self.uiStructureTREE.clear()
    xstruct = self.scaffold().structure()
    self._structure = xstruct
    for xentry in xstruct:
        XScaffoldElementItem(tree, xentry)
    tree.blockSignals(False)
    tree.setUpdatesEnabled(True)