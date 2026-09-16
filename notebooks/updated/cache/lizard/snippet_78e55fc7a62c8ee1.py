def add_eps(self, eps):
    _nodeids, _eps, _vars = self._nodeids, self._eps, self._vars
    for ep in eps:
        try:
            if not isinstance(ep, ElementaryPredication):
                ep = ElementaryPredication(*ep)
        except TypeError:
            raise XmrsError('Invalid EP data: {}'.format(repr(ep)))
        nodeid, lbl = ep.nodeid, ep.label
        if nodeid in _eps:
            raise XmrsError('EP already exists in Xmrs: {} ({})'.format(
                nodeid, ep[1]))
        _nodeids.append(nodeid)
        _eps[nodeid] = ep
        if lbl is not None:
            _vars[lbl]['refs']['LBL'].append(nodeid)
        for role, val in ep.args.items():
            if val in _vars or var_re.match(val):
                vardict = _vars[val]
                vardict['refs'][role].append(nodeid)