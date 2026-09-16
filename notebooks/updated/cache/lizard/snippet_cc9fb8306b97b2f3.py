def set_dict_options(self, options):
    if isinstance(options, dict):
        for key, option_data in options.items():
            self.set_options(key, option_data)
    else:
        raise OptionTypeError(
            'Not An Accepted Input Format: %s. Must be Dictionary' % type(
            options))