def path(self, *path):
    path = list(filter(None, path))
    path = self.unprefix(path)
    items = [self.prefix_] + path
    return self.join(*items)