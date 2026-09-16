def _depth(self):
    terminals = [0]
    depth = 1
    for node in self.program:
        if isinstance(node, _Function):
            terminals.append(node.arity)
            depth = max(len(terminals), depth)
        else:
            terminals[-1] -= 1
            while terminals[-1] == 0:
                terminals.pop()
                terminals[-1] -= 1
    return depth - 1