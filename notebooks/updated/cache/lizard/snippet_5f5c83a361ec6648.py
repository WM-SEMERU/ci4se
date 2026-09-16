def match_check(self, regex, fun):
    vals = []
    if isinstance(fun, six.string_types):
        fun = [fun]
    for func in fun:
        try:
            if re.match(regex, func):
                vals.append(True)
            else:
                vals.append(False)
        except Exception:
            log.error('Invalid regular expression: %s', regex)
    return vals and all(vals)