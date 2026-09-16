def qqplot(pv, distr='log10', alphaLevel=0.05):
    shape_ok = len(pv.shape) == 1 or len(pv.shape) == 2 and pv.shape[1] == 1
    assert shape_ok, 'qqplot requires a 1D array of p-values'
    tests = pv.shape[0]
    pnull = (0.5 + sp.arange(tests)) / tests
    Ipv = sp.argsort(pv)
    if distr == 'chi2':
        qnull = sp.stats.chi2.isf(pnull, 1)
        qemp = sp.stats.chi2.isf(pv[Ipv], 1)
        xl = 'LOD scores'
        yl = '$\\chi^2$ quantiles'
    if distr == 'log10':
        qnull = -sp.log10(pnull)
        qemp = -sp.log10(pv[Ipv])
        xl = '-log10(P) observed'
        yl = '-log10(P) expected'
    line = plt.plot(qnull, qemp, '.')[0]
    plt.plot([0, qnull.max()], [0, qnull.max()], 'r')
    plt.ylabel(xl)
    plt.xlabel(yl)
    if alphaLevel is not None:
        if distr == 'log10':
            betaUp, betaDown, theoreticalPvals = _qqplot_bar(M=tests,
                alphaLevel=alphaLevel, distr=distr)
            lower = -sp.log10(theoreticalPvals - betaDown)
            upper = -sp.log10(theoreticalPvals + betaUp)
            plt.fill_between(-sp.log10(theoreticalPvals), lower, upper,
                color='grey', alpha=0.5)
    return line