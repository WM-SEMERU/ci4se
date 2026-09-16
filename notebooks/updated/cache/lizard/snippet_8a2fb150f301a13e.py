def get_tree(root=None):
    from insights import run
    return run(MultipathConfTree, root=root).get(MultipathConfTree)