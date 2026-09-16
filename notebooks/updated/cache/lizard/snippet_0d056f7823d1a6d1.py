def _register_order_book_channels(self):
    channels = {'order_book': self.btcusd_ob_callback, 'order_book_btceur':
        self.btceur_ob_callback, 'order_book_eurusd': self.
        eurusd_ob_callback, 'order_book_xrpusd': self.xrpusd_ob_callback,
        'order_book_xrpeur': self.xrpeur_ob_callback, 'order_book_xrpbtc':
        self.xrpbtc_ob_callback}
    event = 'data'
    self._bind_channels(event, channels)