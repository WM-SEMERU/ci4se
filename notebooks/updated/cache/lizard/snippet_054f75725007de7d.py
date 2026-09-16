def _ex_type_str(exobj):
    regexp = re.compile("<(?:\\bclass\\b|\\btype\\b)\\s+'?([\\w|\\.]+)'?>")
    exc_type = str(exobj)
    if regexp.match(exc_type):
        exc_type = regexp.match(exc_type).groups()[0]
        exc_type = exc_type[11:] if exc_type.startswith('exceptions.'
            ) else exc_type
    if '.' in exc_type:
        exc_type = exc_type.split('.')[-1]
    return exc_type