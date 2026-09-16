def _shocks_to_epsilons(model, shocks, T):
    n_e = len(model.calibration['exogenous'])
    if isinstance(shocks, pd.DataFrame):
        shocks = {k: shocks[k].tolist() for k in shocks.columns}
    if isinstance(shocks, dict):
        epsilons = np.zeros((T + 1, n_e))
        for i, k in enumerate(model.symbols['exogenous']):
            if k in shocks:
                this_shock = shocks[k]
                epsilons[:len(this_shock), (i)] = this_shock
                epsilons[len(this_shock):, (i)] = this_shock[-1]
            else:
                epsilons[:, (i)] = model.calibration['exogenous'][i]
        return epsilons
    if shocks is None:
        shocks = model.calibration['exogenous']
    shocks = np.asarray(shocks)
    shocks = shocks.reshape((-1, n_e))
    epsilons = np.zeros((T + 1, n_e))
    epsilons[:shocks.shape[0] - 1, :] = shocks[1:, :]
    epsilons[shocks.shape[0] - 1:, :] = shocks[-1:, :]
    return epsilons