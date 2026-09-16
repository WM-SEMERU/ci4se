def network(n):
    tpm(n.tpm)
    connectivity_matrix(n.cm)
    if n.cm.shape[0] != n.size:
        raise ValueError(
            'Connectivity matrix must be NxN, where N is the number of nodes in the network.'
            )
    return True