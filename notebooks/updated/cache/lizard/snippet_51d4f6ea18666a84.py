def check_attr(node, n):
    if len(node.children) > n:
        return node.children[n]