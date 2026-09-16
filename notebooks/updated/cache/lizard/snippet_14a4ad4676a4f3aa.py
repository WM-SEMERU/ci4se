def node_slider(self, seed=None):
    prop = 0.999
    assert isinstance(prop, float), 'prop must be a float'
    assert prop < 1, 'prop must be a proportion >0 and < 1.'
    random.seed(seed)
    ctree = self._ttree.copy()
    for node in ctree.treenode.traverse():
        if node.up and node.children:
            minjit = max([i.dist for i in node.children]) * prop
            maxjit = node.up.height * prop - node.height
            newheight = random.uniform(-minjit, maxjit)
            for child in node.children:
                child.dist += newheight
            node.dist -= newheight
    ctree._coords.update()
    return ctree