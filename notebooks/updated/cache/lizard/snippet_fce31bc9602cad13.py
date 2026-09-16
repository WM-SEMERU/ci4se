def get_options(silent=False, hook=True):
    options_ = {}
    if silent:
        options_['silent'] = silent
    if not hook:
        options_['hook'] = hook
    if options_:
        return '?' + urlencode(options_).lower()
    else:
        return ''