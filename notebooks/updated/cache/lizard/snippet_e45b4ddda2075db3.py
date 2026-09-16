def max_drawdown(returns, out=None):
    allocated_output = out is None
    if allocated_output:
        out = np.empty(returns.shape[1:])
    returns_1d = returns.ndim == 1
    if len(returns) < 1:
        out[()] = np.nan
        if returns_1d:
            out = out.item()
        return out
    returns_array = np.asanyarray(returns)
    cumulative = np.empty((returns.shape[0] + 1,) + returns.shape[1:],
        dtype='float64')
    cumulative[0] = start = 100
    cum_returns(returns_array, starting_value=start, out=cumulative[1:])
    max_return = np.fmax.accumulate(cumulative, axis=0)
    nanmin((cumulative - max_return) / max_return, axis=0, out=out)
    if returns_1d:
        out = out.item()
    elif allocated_output and isinstance(returns, pd.DataFrame):
        out = pd.Series(out)
    return out