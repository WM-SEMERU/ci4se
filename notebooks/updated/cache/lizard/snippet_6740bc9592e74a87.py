def critical(self, event=None, *args, **kw):
    if not self._logger.isEnabledFor(logging.CRITICAL):
        return
    kw = self._add_base_info(kw)
    kw['level'] = 'critical'
    return self._proxy_to_logger('critical', event, *args, **kw)