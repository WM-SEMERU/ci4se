def filetree(self):
    tree = {}
    prefix = []
    paths = (f.split(os.sep) for f in self.files)
    for path in paths:
        dirpath = path[:-1]
        filename = path[-1]
        subtree = tree
        for item in dirpath:
            if item not in subtree:
                subtree[item] = {}
            subtree = subtree[item]
        subtree[filename] = None
    return tree