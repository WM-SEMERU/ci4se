def collapseBefore(self, handle):
    self.setUpdatesEnabled(False)
    if handle.isCollapsed():
        self.setSizes(handle.restoreSizes())
    found = False
    sizes = self.sizes()
    handle.storeSizes(sizes)
    for c in range(self.count()):
        if self.handle(c) == handle:
            break
        sizes[c] = 0
    self.setSizes(sizes)
    self.setUpdatesEnabled(True)