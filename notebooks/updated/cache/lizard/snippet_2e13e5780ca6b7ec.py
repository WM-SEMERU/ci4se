def parse_file(file):
    lines = []
    for line in file:
        line = line.rstrip('\n')
        if line == '%%':
            yield from parse_item(lines)
            lines.clear()
        elif line.startswith('  '):
            lines[-1] += line[1:]
        else:
            lines.append(line)
    yield from parse_item(lines)