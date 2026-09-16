def _tarjan_head(ctx, v):
    ctx.index[v] = len(ctx.index)
    ctx.lowlink[v] = ctx.index[v]
    ctx.S.append(v)
    ctx.S_set.add(v)
    it = iter(ctx.g.get(v, ()))
    ctx.T.append((it, False, v, None))