def _return_retry_timer(self):
    msg = 'Minion return retry timer set to %s seconds'
    if self.opts.get('return_retry_timer_max'):
        try:
            random_retry = randint(self.opts['return_retry_timer'], self.
                opts['return_retry_timer_max'])
            retry_msg = msg % random_retry
            log.debug('%s (randomized)', msg % random_retry)
            return random_retry
        except ValueError:
            log.error(
                'Invalid value (return_retry_timer: %s or return_retry_timer_max: %s). Both must be positive integers.'
                , self.opts['return_retry_timer'], self.opts[
                'return_retry_timer_max'])
            log.debug(msg, DEFAULT_MINION_OPTS['return_retry_timer'])
            return DEFAULT_MINION_OPTS['return_retry_timer']
    else:
        log.debug(msg, self.opts.get('return_retry_timer'))
        return self.opts.get('return_retry_timer')