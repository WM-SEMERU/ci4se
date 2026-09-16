def add_item(self, item):
    item.parent = self
    self.items.append(item)