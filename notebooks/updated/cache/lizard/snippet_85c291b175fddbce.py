def events_log(self, details=False, count=0, timestamp=0):
    if not count:
        count = 1 + int(os.environ.get('ALIGNAK_EVENTS_LOG_COUNT', self.app
            .conf.events_log_count))
    count = int(count)
    timestamp = float(timestamp)
    logger.debug('Get max %d events, newer than %s out of %d', count,
        timestamp, len(self.app.recent_events))
    res = []
    for log in reversed(self.app.recent_events):
        if timestamp and timestamp > log['timestamp']:
            break
        if not count:
            break
        if details:
            res.append(log)
        else:
            res.append('%s - %s - %s' % (log['date'], log['level'][0].upper
                (), log['message']))
    logger.debug('Got %d events', len(res))
    return res