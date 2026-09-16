def _is_cyclic(dag):
    vertices = dag.vertices()
    for w in vertices:
        stack = [w]
        seen = set()
        while stack:
            u = stack.pop()
            seen.add(u)
            for v in dag[u]:
                if v == w:
                    return True
                if v not in seen:
                    stack.append(v)
    return False