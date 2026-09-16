def flat_map(self, func=None, name=None):
    if func is None:
        func = streamsx.topology.runtime._identity
        if name is None:
            name = 'flatten'
    sl = _SourceLocation(_source_info(), 'flat_map')
    _name = self.topology.graph._requested_name(name, action='flat_map',
        func=func)
    stateful = self._determine_statefulness(func)
    op = self.topology.graph.addOperator(self.topology.opnamespace +
        '::FlatMap', func, name=_name, sl=sl, stateful=stateful)
    op.addInputPort(outputPort=self.oport)
    streamsx.topology.schema.StreamSchema._fnop_style(self.oport.schema, op,
        'pyStyle')
    oport = op.addOutputPort(name=_name)
    return Stream(self.topology, oport)._make_placeable()._layout('FlatMap',
        name=_name, orig_name=name)