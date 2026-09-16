def _fS1(self, pos_pairs, A):
    dim = pos_pairs.shape[2]
    diff = pos_pairs[:, (0), :] - pos_pairs[:, (1), :]
    return np.einsum('ij,ik->jk', diff, diff)