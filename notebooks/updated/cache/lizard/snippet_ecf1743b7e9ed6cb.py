def _cleanRecursive(self, subSelf):
    for key, item in list(subSelf.items()):
        if self.isNestedDict(item):
            if not item:
                subSelf.pop(key)
            else:
                self._cleanRecursive(item)