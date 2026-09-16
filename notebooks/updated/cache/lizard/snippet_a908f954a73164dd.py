def checkGeneTreeMatchesSpeciesTree(speciesTree, geneTree, processID):

    def fn(tree, l):
        if tree.internal:
            fn(tree.left, l)
            fn(tree.right, l)
        else:
            l.append(processID(tree.iD))
    l = []
    fn(speciesTree, l)
    l2 = []
    fn(geneTree, l2)
    for i in l2:
        assert i in l