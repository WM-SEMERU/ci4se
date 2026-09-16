def iter_leaves(self, is_leaf_fn=None):
    for n in self.traverse(strategy='preorder', is_leaf_fn=is_leaf_fn):
        if not is_leaf_fn:
            if n.is_leaf():
                yield n
        elif is_leaf_fn(n):
            yield n