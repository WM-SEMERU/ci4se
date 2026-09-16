def guess_type(typ):
    match = re.match('([a-zA-Z]+)\\d*', typ)
    if match:
        typ = match.groups()[0]
        return typ