def _minutes_to_exclude(self):
    market_opens = self._market_opens.values.astype('datetime64[m]')
    market_closes = self._market_closes.values.astype('datetime64[m]')
    minutes_per_day = (market_closes - market_opens).astype(np.int64)
    early_indices = np.where(minutes_per_day != self._minutes_per_day - 1)[0]
    early_opens = self._market_opens[early_indices]
    early_closes = self._market_closes[early_indices]
    minutes = [(market_open, early_close) for market_open, early_close in
        zip(early_opens, early_closes)]
    return minutes