def execute(self):
    self.status = ACT_STATUS_LAUNCHED
    self.check_time = time.time()
    self.wait_time = 0.0001
    self.last_poll = self.check_time
    self.local_env = self.get_local_environnement()
    self.stdoutdata = ''
    self.stderrdata = ''
    logger.debug("Launch command: '%s', ref: %s, timeout: %s", self.command,
        self.ref, self.timeout)
    if self.log_actions:
        if os.environ['ALIGNAK_LOG_ACTIONS'] == 'WARNING':
            logger.warning("Launch command: '%s'", self.command)
        else:
            logger.info("Launch command: '%s'", self.command)
    return self._execute()