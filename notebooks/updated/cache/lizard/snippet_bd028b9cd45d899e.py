def assign_default_log_values(self, fpath, line, formatter):
    return dict(id=None, file=fpath, host=self.HOST, formatter=formatter,
        event='event', data={}, raw=line, timestamp=datetime.datetime.
        utcnow().isoformat(), type='log', level='debug', error=False,
        error_tb='')