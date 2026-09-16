def straddle(self, strike, expiry):
    _rows = {}
    _prices = {}
    for _opttype in _constants.OPTTYPES:
        _rows[_opttype] = _relevant_rows(self.data, (strike, expiry,
            _opttype), 'No key for {} strike {} {}'.format(expiry, strike,
            _opttype))
        _prices[_opttype] = _getprice(_rows[_opttype])
    _eq = _rows[_constants.OPTTYPES[0]].loc[:, ('Underlying_Price')].values[0]
    _qt = _rows[_constants.OPTTYPES[0]].loc[:, ('Quote_Time')].values[0]
    _index = ['Call', 'Put', 'Credit', 'Underlying_Price', 'Quote_Time']
    _vals = np.array([_prices['call'], _prices['put'], _prices['call'] +
        _prices['put'], _eq, _qt])
    return pd.DataFrame(_vals, index=_index, columns=['Value'])