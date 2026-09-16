def process(self, metric, handler):
    match = self.regexp.match(metric.path)
    if match:
        minimum = Minimum(metric.value, self.min)
        maximum = Maximum(metric.value, self.max)
        if minimum.is_error or maximum.is_error:
            self.counter_errors += 1
            message = '%s Warning on %s: %.1f' % (self.name, handler.
                hostname, metric.value)
            culprit = '%s %s' % (handler.hostname, match.group('path'))
            handler.raven_logger.error(message, extra={'culprit': culprit,
                'data': {'metric prefix': match.group('prefix'),
                'metric path': match.group('path'), 'minimum check':
                minimum.verbose_message, 'maximum check': maximum.
                verbose_message, 'metric original path': metric.path,
                'metric value': metric.value, 'metric precision': metric.
                precision, 'metric timestamp': metric.timestamp,
                'minimum threshold': self.min, 'maximum threshold': self.
                max, 'path regular expression': self.regexp.pattern,
                'total errors': self.counter_errors, 'total pass': self.
                counter_pass, 'hostname': handler.hostname}})
        else:
            self.counter_pass += 1