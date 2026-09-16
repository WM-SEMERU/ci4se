def prepare_graph_for_ui(graph, limit_attr_size=1024, large_attrs_key=
    '_too_large_attrs'):
    if limit_attr_size is not None:
        if large_attrs_key is None:
            raise ValueError(
                'large_attrs_key must be != None when limit_attr_size!= None.')
        if limit_attr_size <= 0:
            raise ValueError('limit_attr_size must be > 0, but is %d' %
                limit_attr_size)
    if limit_attr_size is not None:
        for node in graph.node:
            keys = list(node.attr.keys())
            for key in keys:
                size = node.attr[key].ByteSize()
                if size > limit_attr_size or size < 0:
                    del node.attr[key]
                    node.attr[large_attrs_key].list.s.append(tf.compat.
                        as_bytes(key))