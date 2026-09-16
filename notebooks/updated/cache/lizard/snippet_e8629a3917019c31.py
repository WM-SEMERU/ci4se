def load_sanitizers(self, config_data):
    section_strategy = config_data.get('strategy')
    if not isinstance(section_strategy, dict):
        if section_strategy is None:
            return
        raise ConfigurationError("'strategy' is %s instead of dict" % (type
            (section_strategy),))
    for table_name, column_data in six.iteritems(section_strategy):
        if not isinstance(column_data, dict):
            if column_data is None:
                continue
            raise ConfigurationError("'strategy.%s' is %s instead of dict" %
                (table_name, type(column_data)))
        for column_name, sanitizer_name in six.iteritems(column_data):
            if sanitizer_name is None:
                continue
            if not isinstance(sanitizer_name, six.text_type):
                raise ConfigurationError(
                    "'strategy.%s.%s' is %s instead of string" % (
                    table_name, column_name, type(sanitizer_name)))
            sanitizer_callback = self.find_sanitizer(sanitizer_name)
            sanitizer_key = '%s.%s' % (table_name, column_name)
            self.sanitizers[sanitizer_key] = sanitizer_callback