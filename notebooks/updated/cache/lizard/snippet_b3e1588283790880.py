def add_failed_check_attempt(self, reason=''):
    self.reachable = False
    self.attempt = self.attempt + 1
    logger.debug('Failed attempt for %s (%d/%d), reason: %s', self.name,
        self.attempt, self.max_check_attempts, reason)
    if self.alive:
        if not self.stopping:
            logger.warning('Add failed attempt for %s (%d/%d) - %s', self.
                name, self.attempt, self.max_check_attempts, reason)
        else:
            logger.info(
                'Stopping... failed attempt for %s (%d/%d) - also probably stopping'
                , self.name, self.attempt, self.max_check_attempts)
    if self.attempt >= self.max_check_attempts:
        if not self.stopping:
            logger.warning(
                'Set %s as dead, too much failed attempts (%d), last problem is: %s'
                , self.name, self.max_check_attempts, reason)
        else:
            logger.info(
                'Stopping... set %s as dead, too much failed attempts (%d)',
                self.name, self.max_check_attempts)
        self.set_dead()