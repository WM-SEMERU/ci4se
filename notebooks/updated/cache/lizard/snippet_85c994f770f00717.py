def _blank_param_value(value):
    sval = str(value)
    if sval.isspace():
        before, after = '', sval
    else:
        match = re.search('^(\\s*).*?(\\s*)$', sval, FLAGS)
        before, after = match.group(1), match.group(2)
    value.nodes = [Text(before), Text(after)]