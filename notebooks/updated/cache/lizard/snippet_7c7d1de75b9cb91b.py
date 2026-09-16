def _warning(self, msg, duration=None, results=None):
    logger.warning('{} ({})'.format(msg, self._get_logging_id()), extra=
        self._get_logging_extra(duration=duration, results=results))