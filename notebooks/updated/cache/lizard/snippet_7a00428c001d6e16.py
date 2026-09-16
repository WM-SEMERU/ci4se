def is_requirement(line):
    return not (line == '' or line.startswith('-r') or line.startswith('#') or
        line.startswith('-e') or line.startswith('git+'))