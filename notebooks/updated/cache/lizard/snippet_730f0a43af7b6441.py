def calc_trades(current_contracts, desired_holdings, trade_weights, prices,
    multipliers, **kwargs):
    if not isinstance(trade_weights, dict):
        trade_weights = {'': trade_weights}
    generics = []
    for key in trade_weights:
        generics.extend(trade_weights[key].columns)
    if not set(desired_holdings.index).issubset(set(generics)):
        raise ValueError(
            """'desired_holdings.index' contains values which cannot be mapped to tradeables.
Received: 'desired_holdings.index'
 {0}
Expected in 'trade_weights' set of columns:
 {1}
"""
            .format(sorted(desired_holdings.index), sorted(generics)))
    desired_contracts = []
    for root_key in trade_weights:
        gnrc_weights = trade_weights[root_key]
        subset = gnrc_weights.columns.intersection(desired_holdings.index)
        gnrc_des_hlds = desired_holdings.loc[subset]
        gnrc_weights = gnrc_weights.loc[:, (subset)]
        gnrc_weights = gnrc_weights.loc[~(gnrc_weights == 0).all(axis=1)]
        instr_des_hlds = gnrc_des_hlds * gnrc_weights
        instr_des_hlds = instr_des_hlds.sum(axis=1)
        wprices = prices.loc[instr_des_hlds.index]
        desired_contracts.append(to_contracts(instr_des_hlds, wprices,
            multipliers, **kwargs))
    desired_contracts = pd.concat(desired_contracts, axis=0)
    trades = desired_contracts.subtract(current_contracts, fill_value=0)
    trades = trades.loc[trades != 0]
    trades = trades.sort_index()
    return trades