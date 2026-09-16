def aux_moveTree(offset, tree):
    if tree.x1 != None and tree.x2 != None:
        tree.x1, tree.x2 = tree.x1 + offset, tree.x2 + offset
    for c in tree.children:
        aux_moveTree(offset, c)