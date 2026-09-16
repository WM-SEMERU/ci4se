def max_drawdown(returns=None, geometric=True, dd=None, inc_date=False):
    if (returns is None and dd is None or returns is not None and dd is not
        None):
        raise ValueError('returns and drawdowns are mutually exclusive')
    if returns is not None:
        dd = drawdowns(returns, geometric=geometric)
    if isinstance(dd, pd.DataFrame):
        vals = [max_drawdown(dd=dd[c], inc_date=inc_date) for c in dd.columns]
        cols = ['maxxdd'] + (inc_date and ['maxdd_dt'] or [])
        res = pd.DataFrame(vals, columns=cols, index=dd.columns)
        return res if inc_date else res.maxdd
    else:
        mddidx = dd.idxmin()
        sub = dd[:mddidx]
        start = sub[::-1].idxmax()
        mdd = dd[mddidx]
        return mdd if not inc_date else (mdd, mddidx)