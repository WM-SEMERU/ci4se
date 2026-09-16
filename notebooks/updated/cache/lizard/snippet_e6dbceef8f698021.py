def wrap_formatter(formatter):
    if isinstance(formatter, ticker.Formatter):
        return formatter
    elif callable(formatter):
        args = [arg for arg in _getargspec(formatter).args if arg != 'self']
        wrapped = formatter
        if len(args) == 1:

            def wrapped(val, pos=None):
                return formatter(val)
        return ticker.FuncFormatter(wrapped)
    elif isinstance(formatter, basestring):
        if re.findall('\\{(\\w+)\\}', formatter):
            return ticker.StrMethodFormatter(formatter)
        else:
            return ticker.FormatStrFormatter(formatter)