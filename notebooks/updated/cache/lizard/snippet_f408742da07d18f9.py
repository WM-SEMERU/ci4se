def setup(self):
    if self.mlogfilter.is_stdin:
        now = datetime.now()
        self.startDateTime = datetime(now.year, 1, 1, tzinfo=tzutc())
        self.endDateTime = datetime(MAXYEAR, 12, 31, tzinfo=tzutc())
    else:
        logfiles = self.mlogfilter.args['logfile']
        self.startDateTime = min([(lf.start + timedelta(hours=self.
            mlogfilter.args['timezone'][i])) for i, lf in enumerate(logfiles)])
        self.endDateTime = max([(lf.end + timedelta(hours=self.mlogfilter.
            args['timezone'][i])) for i, lf in enumerate(logfiles)])
    dtbound = DateTimeBoundaries(self.startDateTime, self.endDateTime)
    self.fromDateTime, self.toDateTime = dtbound(self.mlogfilter.args[
        'from'] or None, self.mlogfilter.args['to'] or None)
    self.start_limit = self.fromDateTime
    if len(self.mlogfilter.args['logfile']
        ) == 1 and not self.mlogfilter.is_stdin:
        if self.mlogfilter.args['to'] != 'end':
            logfile = self.mlogfilter.args['logfile'][0]
            logfile.fast_forward(self.toDateTime)
            self.seek_to = logfile.filehandle.tell()
            logfile.filehandle.seek(0)
        else:
            self.seek_to = -1
    else:
        self.seek_to = False