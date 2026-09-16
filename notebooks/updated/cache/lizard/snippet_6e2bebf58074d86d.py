def pprint_value(self, value):
    own_type = type(value) if self.type is None else self.type
    formatter = (self.value_format if self.value_format else self.
        type_formatters.get(own_type))
    if formatter:
        if callable(formatter):
            return formatter(value)
        elif isinstance(formatter, basestring):
            if isinstance(value, (dt.datetime, dt.date)):
                return value.strftime(formatter)
            elif isinstance(value, np.datetime64):
                return util.dt64_to_dt(value).strftime(formatter)
            elif re.findall('\\{(\\w+)\\}', formatter):
                return formatter.format(value)
            else:
                return formatter % value
    return unicode(bytes_to_unicode(value))