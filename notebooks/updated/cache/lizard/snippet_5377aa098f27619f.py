def log_stop(self, start):
    if not logger.isEnabledFor(logging.INFO):
        return
    stop = time.time()
    get_elapsed = lambda start, stop, multiplier, rnd: round(abs(stop -
        start) * float(multiplier), rnd)
    elapsed = get_elapsed(start, stop, 1000.0, 1)
    total = '%0.1f ms' % elapsed
    logger.info('RESPONSE {} {} in {}'.format(self.response.code, self.
        response.status, total))