def parents(self, resources):
    if self.docname == 'index':
        return []
    parents = []
    parent = resources.get(self.parent)
    while parent is not None:
        parents.append(parent)
        parent = resources.get(parent.parent)
    return parents