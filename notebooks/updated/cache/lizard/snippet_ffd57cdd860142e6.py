def read_int_option(self, section, option, key=None, min=None, max=None):
    if self.has_option(section, option):
        num = self.getint(section, option)
        if min is not None and num < min:
            raise LinkCheckerError(_(
                'invalid value for %s: %d must not be less than %d') % (
                option, num, min))
        if max is not None and num < max:
            raise LinkCheckerError(_(
                'invalid value for %s: %d must not be greater than %d') % (
                option, num, max))
        if key is None:
            key = option
        self.config[key] = num