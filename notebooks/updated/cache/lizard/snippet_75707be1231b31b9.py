def mcp_als(X, rank, mask, random_state=None, init='randn', **options):
    optim_utils._check_cpd_inputs(X, rank)
    U, _ = optim_utils._get_initial_ktensor(init, X, rank, random_state,
        scale_norm=False)
    result = FitResult(U, 'MCP_ALS', **options)
    normX = np.linalg.norm(X * mask)
    while result.still_optimizing:
        for n in range(X.ndim):
            U.rebalance()
            unf = unfold(X, n)
            m = unfold(mask, n)
            components = [U[j] for j in range(X.ndim) if j != n]
            krt = khatri_rao(components).T
            lhs_stack = np.matmul(m[:, (None), :] * krt[(None), :, :], krt.
                T[(None), :, :])
            rhs_stack = np.dot(unf * m, krt.T)[:, :, (None)]
            U[n] = np.linalg.solve(lhs_stack, rhs_stack).reshape(X.shape[n],
                rank)
        obj = linalg.norm(mask * (U.full() - X)) / normX
        result.update(obj)
    return result.finalize()