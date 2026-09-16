def _insert_data(self, name, value, timestamp, interval, config, **kwargs):
    kwargs = {'name': name, 'interval': interval, 'insert_time': time.time(
        ), 'i_time': config['i_calc'].to_bucket(timestamp), 'value': value}
    if not config['coarse']:
        kwargs['r_time'] = config['r_calc'].to_bucket(timestamp)
    stmt = self._table.insert().values(**kwargs)
    conn = self._client.connect()
    result = conn.execute(stmt)