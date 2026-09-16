def ladderize(self, direction=0):
    nself = deepcopy(self)
    nself.treenode.ladderize(direction=direction)
    nself._fixed_order = None
    nself._coords.update()
    return nself