def load_rules(self):
    for rule_name in self.config.sections():
        limit = 1
        try:
            limit = self.config.getint(rule_name, 'limit')
        except ValueError:
            warnings.warn(
                "Rule '{0}': invalid value for 'limit' option. Limit must be an integer > 0. Going on with the default value of 1."
                .format(rule_name))
        except configparser.NoOptionError:
            warnings.warn(
                "Rule '{0}': no value specified for 'limit' option. Going on with the default value of 1."
                .format(rule_name))
        try:
            filter_str = self.config.get(rule_name, 'filter')
            action_str = self.config.get(rule_name, 'action')
        except configparser.NoOptionError as e:
            warnings.warn("Ignoring '{0}' rule: {1}.".format(rule_name, e))
        else:
            try:
                rule = Rule(rule_name, filter_str, limit, action_str)
            except ValueError as e:
                warnings.warn("Ignoring '{0}' rule: {1}.".format(rule_name, e))
            else:
                self.rules.append(rule)
    if not self.rules:
        raise NoRuleError()
    return self