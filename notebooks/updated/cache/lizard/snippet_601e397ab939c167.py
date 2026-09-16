def analyze_logfile_object(self, file_object):
    log_parser = LogParser()
    if self._start_time is None:
        self._start_time = datetime.now()
        if self._timeout != 0:
            self._end_time = self._start_time + timedelta(minutes=self._timeout
                )
        else:
            self._end_time = None
    for line in file_object:
        if self._end_time is not None and datetime.now() > self._end_time:
            self._run_stats['timedOut'] = True
            self._run_stats['timeoutInMinutes'] = self._timeout
            break
        self._process_query(line, log_parser)
    return 0