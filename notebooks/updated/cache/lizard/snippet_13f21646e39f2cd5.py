def on_failure(self, exc, task_id, args, kwargs, einfo):
    key = self._get_cache_key(args, kwargs)
    _, penalty = cache.get(key, (0, 0))
    if penalty < self.MAX_PENALTY:
        penalty += 1
    logger.debug('The task %s is penalized and will be executed on %d run.' %
        (self.name, penalty))
    cache.set(key, (penalty, penalty), self.CACHE_LIFETIME)
    return super(PenalizedBackgroundTask, self).on_failure(exc, task_id,
        args, kwargs, einfo)