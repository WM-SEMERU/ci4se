def backtrace_root(node):
    rpath = []
    prev = node
    now = node.parent
    while now is not None:
        if now.left is prev:
            rpath.append((now, 0))
        elif now.right is prev:
            rpath.append((now, 1))
        else:
            raise AssertionError('impossible state')
        prev = now
        now = now.parent
    return rpath