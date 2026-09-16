def icon(self, *names, **kwargs):
    cache_key = '{}{}'.format(names, kwargs)
    if cache_key not in self.icon_cache:
        options_list = kwargs.pop('options', [{}] * len(names))
        general_options = kwargs
        if len(options_list) != len(names):
            error = '"options" must be a list of size {0}'.format(len(names))
            raise Exception(error)
        if QApplication.instance() is not None:
            parsed_options = []
            for i in range(len(options_list)):
                specific_options = options_list[i]
                parsed_options.append(self._parse_options(specific_options,
                    general_options, names[i]))
            api_options = parsed_options
            self.icon_cache[cache_key] = self._icon_by_painter(self.painter,
                api_options)
        else:
            warnings.warn(
                'You need to have a running QApplication to use QtAwesome!')
            return QIcon()
    return self.icon_cache[cache_key]