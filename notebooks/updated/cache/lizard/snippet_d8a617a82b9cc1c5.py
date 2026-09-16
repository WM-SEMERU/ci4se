def height(self):
    min_height = int(bool(self))
    return max([min_height] + [(c.height() + 1) for c, p in self.children])