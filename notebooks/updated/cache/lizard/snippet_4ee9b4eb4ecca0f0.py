def split(coll, factor):
    groups = groupby(lambda x: x[0], itertools.izip(factor, coll))
    return dmap(lambda x: [y[1] for y in x], groups)