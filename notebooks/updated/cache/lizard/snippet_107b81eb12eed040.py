def metrics(self, opttype, strike, expiry):
    _optrow = _relevant_rows(self.data, (strike, expiry, opttype),
        'No key for {} strike {} {}'.format(expiry, strike, opttype))
    _index = ['Opt_Price', 'Time_Val', 'Last', 'Bid', 'Ask', 'Vol',
        'Open_Int', 'Underlying_Price', 'Quote_Time']
    _out = pd.DataFrame(index=_index, columns=['Value'])
    _out.loc['Opt_Price', 'Value'] = _opt_price = _getprice(_optrow)
    for _name in _index[2:]:
        _out.loc[_name, 'Value'] = _optrow.loc[:, (_name)].values[0]
    _eq_price = _out.loc['Underlying_Price', 'Value']
    if opttype == 'put':
        _out.loc['Time_Val'] = _get_put_time_val(_opt_price, strike, _eq_price)
    else:
        _out.loc['Time_Val'] = _get_call_time_val(_opt_price, strike, _eq_price
            )
    return _out