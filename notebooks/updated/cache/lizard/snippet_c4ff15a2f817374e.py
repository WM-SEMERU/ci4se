def annual_volatility(returns, period=DAILY, alpha=2.0, annualization=None,
    out=None):
    allocated_output = out is None
    if allocated_output:
        out = np.empty(returns.shape[1:])
    returns_1d = returns.ndim == 1
    if len(returns) < 2:
        out[()] = np.nan
        if returns_1d:
            out = out.item()
        return out
    ann_factor = annualization_factor(period, annualization)
    nanstd(returns, ddof=1, axis=0, out=out)
    out = np.multiply(out, ann_factor ** (1.0 / alpha), out=out)
    if returns_1d:
        out = out.item()
    return out