def sortino_ratio(returns, required_return=0, period=DAILY, annualization=
    None, out=None, _downside_risk=None):
    allocated_output = out is None
    if allocated_output:
        out = np.empty(returns.shape[1:])
    return_1d = returns.ndim == 1
    if len(returns) < 2:
        out[()] = np.nan
        if return_1d:
            out = out.item()
        return out
    adj_returns = np.asanyarray(_adjust_returns(returns, required_return))
    ann_factor = annualization_factor(period, annualization)
    average_annual_return = nanmean(adj_returns, axis=0) * ann_factor
    annualized_downside_risk = (_downside_risk if _downside_risk is not
        None else downside_risk(returns, required_return, period,
        annualization))
    np.divide(average_annual_return, annualized_downside_risk, out=out)
    if return_1d:
        out = out.item()
    elif isinstance(returns, pd.DataFrame):
        out = pd.Series(out)
    return out