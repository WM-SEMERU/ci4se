def state_by_state2state_by_node(tpm):
    tpm = np.array(tpm)
    S = tpm.shape[-1]
    N = int(log2(S))
    sbn_tpm = np.zeros([2] * N + [N])
    states = {i: le_index2state(i, N) for i in range(S)}
    node_on = np.array([[states[i][n] for i in range(S)] for n in range(N)])
    on_probabilities = [(tpm * node_on[n]) for n in range(N)]
    for i, state in states.items():
        sbn_tpm[state] = [np.sum(on_probabilities[n][i]) for n in range(N)]
    return sbn_tpm