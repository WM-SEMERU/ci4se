def _matchPattern(regExp, string):
    match = regExp.match(string)
    if match is not None and match.group(0):
        return match.group(0), (match.group(0),) + match.groups()
    else:
        return None, None