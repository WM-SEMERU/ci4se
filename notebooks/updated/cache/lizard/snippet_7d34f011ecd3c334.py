def determine_coverage(cls, coverage_file):
    lines = []
    source_file = 'ERROR'
    for line in coverage_file:
        m = title_re.match(line)
        if m:
            if m.group(2) == '100':
                return '', []
            source_file = m.group(1)
            continue
        m = source_re.match(line)
        if m:
            lines.append(int(m.group(1)))
            continue
        if end_re.match(line):
            break
    line_ranges = cls.make_ranges(lines)
    return source_file, line_ranges