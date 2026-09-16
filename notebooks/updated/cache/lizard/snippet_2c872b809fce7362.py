def unittree(ntips, treeheight=1.0, seed=None):
    random.seed(seed)
    tmptree = TreeNode()
    tmptree.populate(ntips)
    self = toytree.tree(newick=tmptree.write())
    self = self.ladderize().mod.make_ultrametric().mod.node_scale_root_height(
        treeheight)
    nidx = list(range(self.ntips))
    random.shuffle(nidx)
    for tidx, node in enumerate(self.treenode.get_leaves()):
        node.name = 'r{}'.format(nidx[tidx])
    self._coords.update()
    return self