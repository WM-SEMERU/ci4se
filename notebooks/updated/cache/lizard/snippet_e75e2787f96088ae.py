def use_quandl_data(self, authtoken):
    dfs = {}
    st = self.start.strftime('%Y-%m-%d')
    at = authtoken
    for pair in self.pairs:
        symbol = ''.join(pair)
        qsym = 'CURRFX/{}'.format(symbol)
        dfs[symbol] = qdl.get(qsym, authtoken=at, trim_start=st)['Rate']
    self.build_conversion_table(dfs)