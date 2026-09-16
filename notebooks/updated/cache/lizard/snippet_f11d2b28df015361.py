def _is_requirement(line):
    line = line.strip()
    return line and not (line.startswith('-r') or line.startswith('#'))