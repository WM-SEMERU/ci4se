def distance_between(self, u, v):
    if not isinstance(u, Node):
        raise TypeError('u must be a Node')
    if not isinstance(v, Node):
        raise TypeError('v must be a Node')
    if u == v:
        return 0.0
    u_dists = {u: 0.0}
    v_dists = {v: 0.0}
    c = u
    p = u.parent
    while p is not None:
        u_dists[p] = u_dists[c]
        if c.edge_length is not None:
            u_dists[p] += c.edge_length
        c = p
        p = p.parent
    c = v
    p = v.parent
    while p is not None:
        v_dists[p] = v_dists[c]
        if c.edge_length is not None:
            v_dists[p] += c.edge_length
        if p in u_dists:
            return u_dists[p] + v_dists[p]
        c = p
        p = p.parent
    raise RuntimeError('u and v are not in the same Tree')