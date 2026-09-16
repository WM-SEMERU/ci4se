def exception(self, event=None, *args, **kw):
    if not self._logger.isEnabledFor(logging.ERROR):
        return
    kw = self._add_base_info(kw)
    kw['level'] = 'exception'
    kw.setdefault('exc_info', True)
    return self.error(event, *args, **kw)