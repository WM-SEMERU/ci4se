def get_kline_data(self, symbol, kline_type='5min', start=None, end=None):
    data = {'symbol': symbol}
    if kline_type is not None:
        data['type'] = kline_type
    if start is not None:
        data['startAt'] = start
    else:
        data['startAt'] = calendar.timegm(datetime.utcnow().date().timetuple())
    if end is not None:
        data['endAt'] = end
    else:
        data['endAt'] = int(time.time())
    return self._get('market/candles', False, data=data)