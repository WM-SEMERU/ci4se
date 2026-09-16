def convert(cls, tree):
    if isinstance(tree, Tree):
        children = [cls.convert(child) for child in tree]
        if isinstance(tree, MetricalTree):
            return cls(tree._cat, children, tree._dep, tree._lstress)
        elif isinstance(tree, DependencyTree):
            return cls(tree._cat, children, tree._dep)
        else:
            return cls(tree._label, children)
    else:
        return tree