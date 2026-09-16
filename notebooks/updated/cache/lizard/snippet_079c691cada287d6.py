def _run_queued_callbacks(self):
    for callback in self._queued_callbacks:
        try:
            callback()
        except Exception as ex:
            logger.error('Exception: %s' % str(ex))