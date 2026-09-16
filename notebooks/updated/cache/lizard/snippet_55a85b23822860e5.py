def _mfpts(tprob, populations, sinks, lag_time):
    n_states = np.shape(populations)[0]
    if sinks is None:
        limiting_matrix = np.vstack([populations] * n_states)
        fund_matrix = scipy.linalg.inv(np.eye(n_states) - tprob +
            limiting_matrix)
        mfpts = fund_matrix * -1
        for j in xrange(n_states):
            mfpts[:, (j)] += fund_matrix[j, j]
            mfpts[:, (j)] /= populations[j]
        mfpts *= lag_time
    else:
        sinks = np.array(sinks, dtype=int).reshape((-1,))
        absorb_tprob = copy.copy(tprob)
        for state in sinks:
            absorb_tprob[(state), :] = 0.0
            absorb_tprob[state, state] = 2.0
        lhs = np.eye(n_states) - absorb_tprob
        rhs = np.ones(n_states)
        for state in sinks:
            rhs[state] = 0.0
        mfpts = lag_time * np.linalg.solve(lhs, rhs)
    return mfpts