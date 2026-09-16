def parse_multi_value_header(header_str):
    parsed_parts = []
    if header_str:
        parts = header_str.split(',')
        for part in parts:
            match = re.search('\\s*(W/)?"?([^"]*)"?\\s*', part)
            if match is not None:
                parsed_parts.append(match.group(2))
    return parsed_parts