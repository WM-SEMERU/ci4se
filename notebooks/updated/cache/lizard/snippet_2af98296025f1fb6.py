def indirectInitialMatrix(self, initialState):
    mapping = {}
    rates = OrderedDict()
    convertedState = self.checkInitialState(initialState)
    if isinstance(convertedState, set):
        frontier = set(convertedState)
        for idx, state in enumerate(convertedState):
            mapping[state] = idx
            if idx == 0:
                usesNumpy = self.checkTransitionType(initialState)
    else:
        frontier = set([convertedState])
        usesNumpy = self.checkTransitionType(initialState)
        mapping[convertedState] = 0
    while len(frontier) > 0:
        fromstate = frontier.pop()
        fromindex = mapping[fromstate]
        if usesNumpy:
            transitions = self.transition(np.array(fromstate))
            transitions = self.convertToTransitionDict(transitions)
        else:
            transitions = self.transition(fromstate)
        for tostate, rate in transitions.items():
            if tostate not in mapping:
                frontier.add(tostate)
                mapping[tostate] = len(mapping)
            toindex = mapping[tostate]
            rates[fromindex, toindex] = rate
    self.mapping = {value: key for key, value in list(mapping.items())}
    D = dok_matrix((self.size, self.size))
    D.update(rates)
    return D.tocsr()