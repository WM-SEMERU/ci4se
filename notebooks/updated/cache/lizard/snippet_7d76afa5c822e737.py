def watch_for_new_conf(self, timeout=0):
    logger.debug('Watching for a new configuration, timeout: %s', timeout)
    self.make_a_pause(timeout=timeout, check_time_change=False)
    return any(self.new_conf)