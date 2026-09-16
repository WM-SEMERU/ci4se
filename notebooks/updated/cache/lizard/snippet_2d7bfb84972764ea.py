def get_option_default(self, opt_name):
    if not self.has_option(opt_name):
        raise ValueError('Unknow option name (%s)' % opt_name)
    return self._options[opt_name].default