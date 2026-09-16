def add_child(self, item):
    item.depth = self.depth + 1
    self.childs.append(item)
    self.childs = sorted(self.childs, key=lambda item: item.order if item.
        order else 999)