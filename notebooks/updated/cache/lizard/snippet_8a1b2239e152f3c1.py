def _register_live_trades_channels(self):
    channels = {'live_trades': self.btcusd_lt_callback,
        'live_trades_btceur': self.btceur_lt_callback, 'live_trades_eurusd':
        self.eurusd_lt_callback, 'live_trades_xrpusd': self.
        xrpusd_lt_callback, 'live_trades_xrpeur': self.xrpeur_lt_callback,
        'live_trades_xrpbtc': self.xrpbtc_lt_callback}
    event = 'trade'
    self._bind_channels(event, channels)