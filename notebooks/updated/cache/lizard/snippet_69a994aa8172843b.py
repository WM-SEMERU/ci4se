def parse_upstring(line):
    UP_STRING_REGEX = '\\[(U|_)+]'
    match = re.search(UP_STRING_REGEX, line)
    if match:
        return match.group().strip('[]')
    else:
        return None