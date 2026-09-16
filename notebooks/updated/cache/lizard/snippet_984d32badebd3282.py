def get_metric_by_day(self, unique_identifier, metric, from_date, limit=30,
    **kwargs):
    conn = kwargs.get('connection', None)
    date_generator = (from_date + datetime.timedelta(days=i) for i in
        itertools.count())
    metric_key_date_range = self._get_daily_date_range(from_date, datetime.
        timedelta(days=limit))
    series = list(itertools.islice(date_generator, limit))
    metric_keys = [self._get_daily_metric_name(metric, daily_date) for
        daily_date in series]
    metric_func = lambda conn: [conn.hmget(self._get_daily_metric_key(
        unique_identifier, metric_key_date), metric_keys) for
        metric_key_date in metric_key_date_range]
    if conn is not None:
        results = metric_func(conn)
    else:
        with self._analytics_backend.map() as conn:
            results = metric_func(conn)
        series, results = self._parse_and_process_metrics(series, results)
    return series, results