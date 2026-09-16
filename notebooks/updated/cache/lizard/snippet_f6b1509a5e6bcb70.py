def find_usage(self):
    logger.debug('Checking usage for service %s', self.service_name)
    self.connect()
    for lim in self.limits.values():
        lim._reset_usage()
    self._find_usage_instances()
    self._find_usage_subnet_groups()
    self._find_usage_security_groups()
    self._update_limits_from_api()
    self._have_usage = True
    logger.debug('Done checking usage.')