def parse_line(line):
    line = line.rstrip()
    line_type = _get_line_type(line)
    return TabLine(type=line_type, data=_DATA_PARSERS[line_type](line),
        original=line)