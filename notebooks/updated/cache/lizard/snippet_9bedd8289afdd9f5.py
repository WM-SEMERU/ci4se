def suppress_unifurcations(self):
    q = deque()
    q.append(self.root)
    while len(q) != 0:
        node = q.popleft()
        if len(node.children) != 1:
            q.extend(node.children)
            continue
        child = node.children.pop()
        if node.is_root():
            self.root = child
            child.parent = None
        else:
            parent = node.parent
            parent.remove_child(node)
            parent.add_child(child)
        if node.edge_length is not None:
            if child.edge_length is None:
                child.edge_length = 0
            child.edge_length += node.edge_length
        if child.label is None and node.label is not None:
            child.label = node.label
        q.append(child)