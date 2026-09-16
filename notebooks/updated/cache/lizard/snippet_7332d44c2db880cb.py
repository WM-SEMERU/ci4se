def _at_debug(self, calculator, rule, scope, block):
    setting = block.argument.strip()
    if setting.lower() in ('1', 'true', 't', 'yes', 'y', 'on'):
        setting = True
    elif setting.lower() in ('0', 'false', 'f', 'no', 'n', 'off', 'undefined'):
        setting = False
    self.ignore_parse_errors = setting
    log.info('Debug mode is %s', 'On' if self.ignore_parse_errors else 'Off')