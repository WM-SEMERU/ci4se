def stream_logs(self, build_id):
    kwargs = {'follow': 1}
    min_idle_timeout = 60
    last_activity = time.time()
    while True:
        buildlogs_url = self._build_url('builds/%s/log/' % build_id, **kwargs)
        try:
            response = self._get(buildlogs_url, stream=1, headers={
                'Connection': 'close'})
            check_response(response)
            for line in response.iter_lines():
                last_activity = time.time()
                yield line
        except OsbsException as exc:
            if not isinstance(exc.cause, ConnectionError):
                raise
        idle = time.time() - last_activity
        logger.debug('connection closed after %ds', idle)
        if idle < min_idle_timeout:
            return
        since = int(idle - 1)
        logger.debug('fetching logs starting from %ds ago', since)
        kwargs['sinceSeconds'] = since