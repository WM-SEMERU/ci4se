def _mark_started(self):
    log = self._params.get('log', self._discard)
    now = time.time()
    self._started = now
    limit = self._config_running.get('time_limit')
    try:
        limit = float(_fmt_context(self._get(limit, default='0'), self.
            _context))
        if limit > 0:
            log.debug("Applying task '%s' time limit of %s", self._name,
                deltafmt(limit))
            self._limit = now + limit
    except Exception as e:
        log.warn("Task '%s' time_limit value '%s' invalid -- %s", self.
            _name, limit, e, exc_info=log.isEnabledFor(logging.DEBUG))