def get_bars(self, lookback=None, as_dict=False):
    bars = self._get_symbol_dataframe(self.parent.bars, self)
    bars = self.parent._add_signal_history(df=bars, symbol=self)
    lookback = self.bar_window if lookback is None else lookback
    bars = bars[-lookback:]
    if not bars.empty > 0 and bars['asset_class'].values[-1] not in ('OPT',
        'FOP'):
        bars.drop(bars.columns[bars.columns.str.startswith('opt_')].tolist(
            ), inplace=True, axis=1)
    if as_dict:
        bars.loc[:, ('datetime')] = bars.index
        bars = bars.to_dict(orient='records')
        if lookback == 1:
            bars = None if not bars else bars[0]
    return bars