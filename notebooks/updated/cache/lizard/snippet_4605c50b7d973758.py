def create(cls, *props, **kwargs):
    if 'streaming' in kwargs:
        warnings.warn(
            'streaming is not supported by bolt, please remove the kwarg',
            category=DeprecationWarning, stacklevel=1)
    lazy = kwargs.get('lazy', False)
    query = 'CREATE (n:{0} {{create_params}})'.format(':'.join(cls.
        inherited_labels()))
    if lazy:
        query += ' RETURN id(n)'
    else:
        query += ' RETURN n'
    results = []
    for item in [cls.deflate(p, obj=_UnsavedNode(), skip_empty=True) for p in
        props]:
        node, _ = db.cypher_query(query, {'create_params': item})
        results.extend(node[0])
    nodes = [cls.inflate(node) for node in results]
    if not lazy and hasattr(cls, 'post_create'):
        for node in nodes:
            node.post_create()
    return nodes