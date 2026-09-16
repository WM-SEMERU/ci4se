def concatenated(fp):
    line_parts = []
    for line in fp:
        line = line.strip()
        if line.endswith('\\'):
            line_parts.append(line[:-1].rstrip())
        else:
            line_parts.append(line)
            yield ' '.join(line_parts)
            line_parts[:] = []
    if line_parts:
        raise RuntimeError('Compiled file ends with backslash \\')