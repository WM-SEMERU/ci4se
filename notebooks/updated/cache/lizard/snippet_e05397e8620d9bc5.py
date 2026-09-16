def get_metric_by_week(self, unique_identifier, metric, from_date, limit=10,
    **kwargs):
    conn = kwargs.get('connection', None)
    closest_monday_from_date = self._get_closest_week(from_date)
    metric_key_date_range = self._get_weekly_date_range(
        closest_monday_from_date, datetime.timedelta(weeks=limit))
    date_generator = (closest_monday_from_date + datetime.timedelta(days=i) for
        i in itertools.count(step=7))
    series = list(itertools.islice(date_generator, limit))
    metric_keys = [self._get_weekly_metric_name(metric, monday_date) for
        monday_date in series]
    metric_func = lambda conn: [conn.hmget(self._get_weekly_metric_key(
        unique_identifier, metric_key_date), metric_keys) for
        metric_key_date in metric_key_date_range]
    if conn is not None:
        results = metric_func(conn)
    else:
        with self._analytics_backend.map() as conn:
            results = metric_func(conn)
        series, results = self._parse_and_process_metrics(series, results)
    return series, results