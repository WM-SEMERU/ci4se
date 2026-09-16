def add_rule_entry(self, rule_info):
    new_rule = IpMacPort(rule_info.get('ip'), rule_info.get('mac'),
        rule_info.get('port'))
    LOG.debug('Added rule info %s to the list', rule_info)
    self.rule_info.append(new_rule)