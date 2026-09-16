def preorder_iter(self, filter_fn=None):
    stack = [self]
    while stack:
        node = stack.pop()
        if filter_fn is None or filter_fn(node):
            yield node
        stack.extend([i for i in reversed(node._children)])