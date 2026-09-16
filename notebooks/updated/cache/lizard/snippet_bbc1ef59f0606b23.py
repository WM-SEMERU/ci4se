def parse(name, content, releases, get_head_fn):
    changelog = {}
    releases = frozenset(releases)
    head = False
    date_line = None
    for line in content.splitlines():
        if DATE_RE.match(line):
            date_line = line
            continue
        if line.strip().startswith('PyAudio'):
            try:
                head = line.strip().split()[1]
            except:
                continue
            changelog[head] = date_line + '\n'
            continue
        if not head:
            continue
        line = line.replace('@', '')
        line = line.replace('#', '')
        changelog[head] += line + '\n'
    return changelog