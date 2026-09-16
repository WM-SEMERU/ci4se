def correlate(params, corrmat):
    assert all([isinstance(param, UncertainFunction) for param in params]
        ), 'All inputs to "correlate" must be of type "UncertainFunction"'
    data = np.vstack([param._mcpts for param in params]).T
    new_data = induce_correlations(data, corrmat)
    for i in range(len(params)):
        params[i]._mcpts = new_data[:, (i)]