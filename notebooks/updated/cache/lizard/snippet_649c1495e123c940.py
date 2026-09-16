def add_macd(self, fast_period=12, slow_period=26, signal_period=9, column=
    None, name='', str=None, **kwargs):
    if not column:
        column = self._d['close']
    study = {'kind': 'macd', 'name': name, 'params': {'fast_period':
        fast_period, 'slow_period': slow_period, 'signal_period':
        signal_period, 'column': column, 'str': str}, 'display': utils.
        merge_dict({'legendgroup': False, 'colors': ['blue', 'red']}, kwargs)}
    study['params']['periods'] = '[{0},{1},{2}]'.format(fast_period,
        slow_period, signal_period)
    self._add_study(study)