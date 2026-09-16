def _set(self, path, value, build_dir=''):
    assert isinstance(path, list) and len(path) > 0
    if isinstance(value, pd.DataFrame):
        metadata = {SYSTEM_METADATA: {'target': TargetType.PANDAS.value}}
    elif isinstance(value, np.ndarray):
        metadata = {SYSTEM_METADATA: {'target': TargetType.NUMPY.value}}
    elif isinstance(value, string_types + (bytes,)):
        value = value.decode() if isinstance(value, bytes) else value
        if os.path.isabs(value):
            raise ValueError(
                'Invalid path: expected a relative path, but received {!r}'
                .format(value))
        metadata = {SYSTEM_METADATA: {'filepath': value, 'transform': 'id'}}
        if build_dir:
            value = os.path.join(build_dir, value)
    else:
        accepted_types = tuple(set((pd.DataFrame, np.ndarray, bytes) +
            string_types))
        raise TypeError(
            'Bad value type: Expected instance of any type {!r}, but received type {!r}'
            .format(accepted_types, type(value)), repr(value)[0:100])
    for key in path:
        if not is_nodename(key):
            raise ValueError('Invalid name for node: {}'.format(key))
    node = self
    for key in path[:-1]:
        child = node._get(key)
        if not isinstance(child, GroupNode):
            child = GroupNode({})
            node[key] = child
        node = child
    key = path[-1]
    node[key] = DataNode(None, None, value, metadata)