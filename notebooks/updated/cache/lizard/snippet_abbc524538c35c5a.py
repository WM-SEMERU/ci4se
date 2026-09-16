def set_node_attributes(G, values, name=None):
    if name is not None:
        try:
            for n, v in values.items():
                try:
                    G.node[n][name] = values[n]
                except KeyError:
                    pass
        except AttributeError:
            for n in G:
                G.node[n][name] = values
    else:
        for n, d in values.items():
            try:
                G.node[n].update(d)
            except KeyError:
                pass