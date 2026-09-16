def syncView(self):
    if not self.updatesEnabled():
        return
    for item in self.topLevelItems():
        try:
            item.syncView(recursive=True)
        except AttributeError:
            continue