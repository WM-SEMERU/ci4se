def fw_rule_create(self, data, fw_name=None, cache=False):
    LOG.debug('FW Rule create %s', data)
    self._fw_rule_create(fw_name, data, cache)