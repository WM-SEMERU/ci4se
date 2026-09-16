def _separate_keyword(line):
    try:
        first, rest = line.split(None, 1)
    except ValueError:
        first = line.strip()
        rest = ''
    return first, rest