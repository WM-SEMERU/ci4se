def _iter_descendants_preorder(self, is_leaf_fn=None):
    to_visit = deque()
    node = self
    while node is not None:
        yield node
        if not is_leaf_fn or not is_leaf_fn(node):
            to_visit.extendleft(reversed(node.children))
        try:
            node = to_visit.popleft()
        except:
            node = None