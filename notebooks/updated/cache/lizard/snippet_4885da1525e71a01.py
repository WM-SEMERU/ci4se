def getTransitionProbabilities(state, action):
    assert 0 <= action < ACTIONS
    if not isLegal(state, action):
        s1 = [convertTupleToIndex(state)]
        return s1, [1], -10
    state = list(state)
    state[action] = PLAYER
    if isWon(state, PLAYER):
        s1 = [convertTupleToIndex(state)]
        return s1, [1], 1
    elif isDraw(state):
        s1 = [convertTupleToIndex(state)]
        return s1, [1], 0
    s1 = []
    p = []
    legal_a = getLegalActions(state)
    for a in legal_a:
        state[a] = OPPONENT
        if isWon(state, OPPONENT):
            s1 = [convertTupleToIndex(state)]
            return s1, [1], -1
        elif isDraw(state):
            s1 = [convertTupleToIndex(state)]
            return s1, [1], 0
        s1.append(convertTupleToIndex(state))
        p.append(1.0 / len(legal_a))
        state[a] = 0
    return s1, p, 0