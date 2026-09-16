def baltree(ntips, treeheight=1.0):
    if ntips % 2:
        raise ToytreeError('balanced trees must have even number of tips.')
    rtree = toytree.tree()
    rtree.treenode.add_child(name='0')
    rtree.treenode.add_child(name='1')
    for i in range(2, ntips):
        node = return_small_clade(rtree.treenode)
        node.add_child(name=node.name)
        node.add_child(name=str(i))
        node.name = None
    idx = 0
    for node in rtree.treenode.traverse('postorder'):
        if node.is_leaf():
            node.name = str(idx)
            idx += 1
    tre = toytree.tree(rtree.write(tree_format=9))
    tre = tre.mod.make_ultrametric()
    self = tre.mod.node_scale_root_height(treeheight)
    self._coords.update()
    return self