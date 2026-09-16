def qualify(ref, resolvers, defns=Namespace.default):
    ns = None
    p, n = splitPrefix(ref)
    if p is not None:
        if not isinstance(resolvers, (list, tuple)):
            resolvers = resolvers,
        for r in resolvers:
            resolved = r.resolvePrefix(p)
            if resolved[1] is not None:
                ns = resolved
                break
        if ns is None:
            raise Exception('prefix (%s) not resolved' % p)
    else:
        ns = defns
    return n, ns[1]