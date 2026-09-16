def prefix_lines(lines, prefix):
    if isinstance(lines, bytes):
        lines = lines.decode('utf-8')
    if isinstance(lines, str):
        lines = lines.splitlines()
    return [(prefix + line) for line in lines]