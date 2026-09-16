def _sample_oat(problem, N, num_levels=4):
    group_membership = np.asmatrix(np.identity(problem['num_vars'], dtype=int))
    num_params = group_membership.shape[0]
    sample = np.zeros((N * (num_params + 1), num_params))
    sample = np.array([generate_trajectory(group_membership, num_levels) for
        n in range(N)])
    return sample.reshape((N * (num_params + 1), num_params))