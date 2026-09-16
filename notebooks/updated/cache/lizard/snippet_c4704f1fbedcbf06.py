def order(self, signal, symbol, quantity=0, **kwargs):
    self.log_algo.debug('ORDER: %s %4d %s %s', signal, quantity, symbol, kwargs
        )
    if signal.upper() == 'EXIT' or signal.upper() == 'FLATTEN':
        position = self.get_positions(symbol)
        if position['position'] == 0:
            return
        kwargs['symbol'] = symbol
        kwargs['quantity'] = abs(position['position'])
        kwargs['direction'] = 'BUY' if position['position'] < 0 else 'SELL'
        try:
            self.record({(symbol + '_POSITION'): 0})
        except Exception as e:
            pass
        if not self.backtest:
            self._create_order(**kwargs)
    else:
        if quantity == 0:
            return
        kwargs['symbol'] = symbol
        kwargs['quantity'] = abs(quantity)
        kwargs['direction'] = signal.upper()
        try:
            quantity = abs(quantity)
            if kwargs['direction'] != 'BUY':
                quantity = -quantity
            self.record({(symbol + '_POSITION'): quantity})
        except Exception as e:
            pass
        if not self.backtest:
            self._create_order(**kwargs)