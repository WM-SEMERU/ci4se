def match_prefix(prefix, line):
    m = re.match(prefix, line.expandtabs(4))
    if not m:
        if re.match(prefix, line.expandtabs(4).replace('\n', ' ' * 99 + '\n')):
            return len(line) - 1
        return -1
    pos = m.end()
    if pos == 0:
        return 0
    for i in range(1, len(line) + 1):
        if len(line[:i].expandtabs(4)) >= pos:
            return i