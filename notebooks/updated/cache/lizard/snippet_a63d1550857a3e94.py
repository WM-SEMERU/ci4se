def _line_parse(line):
    if line[-2:] in ['\r\n', b'\r\n']:
        return line[:-2], True
    elif line[-1:] in ['\r', '\n', b'\r', b'\n']:
        return line[:-1], True
    return line, False