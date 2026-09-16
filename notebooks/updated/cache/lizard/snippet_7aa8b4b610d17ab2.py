def find_usage(self):
    logger.debug('Checking usage for service %s', self.service_name)
    self.connect()
    self.connect_resource()
    for lim in self.limits.values():
        lim._reset_usage()
    self._find_usage_instances()
    self._find_usage_networking_sgs()
    self._find_usage_networking_eips()
    self._find_usage_networking_eni_sg()
    self._find_usage_spot_instances()
    self._find_usage_spot_fleets()
    self._have_usage = True
    logger.debug('Done checking usage.')