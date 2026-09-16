def _parse_jing_output(output):
    output = output.strip()
    values = [_parse_jing_line(l) for l in output.split('\n') if l]
    return tuple(values)