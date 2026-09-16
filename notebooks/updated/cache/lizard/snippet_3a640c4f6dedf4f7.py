def tags(self):
    item = self.item(self.count() - 1)
    count = self.count()
    if item is self._createItem:
        count -= 1
    return [nativestring(self.item(row).text()) for row in range(count)]