def from_file(filename):
    entries = []
    with open(filename) as fd:
        lines = []
        for line in fd.readlines():
            line = line.rstrip()
            if not line:
                if lines:
                    entries.append(from_headers('\r\n'.join(lines)))
                lines = []
            else:
                lines.append(line)
        if lines:
            entries.append(from_headers('\r\n'.join(lines)))
        return entries