def preload_tops(meta):
    top_fns = set(meta['top_fn'])
    tops = {}
    for tfn in top_fns:
        tops[tfn] = md.load_topology(tfn)
    return tops