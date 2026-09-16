def _extract_header_number(lines):
    pair = _extract_header_value(lines[1])
    value_list = list(pair.values())
    return int(value_list[0])