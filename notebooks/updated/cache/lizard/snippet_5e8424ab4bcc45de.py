def get_exitstatus(self):
    logger.debug('Exit status is {0}'.format(self._spawn.exitstatus))
    return self._spawn.exitstatus