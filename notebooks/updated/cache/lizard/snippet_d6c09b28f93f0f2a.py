def ontologyShapeTree(self):
    treedict = {}
    if self.all_shapes:
        treedict[0] = self.toplayer_shapes
        for element in self.all_shapes:
            if element.children():
                treedict[element] = element.children()
        return treedict
    return treedict