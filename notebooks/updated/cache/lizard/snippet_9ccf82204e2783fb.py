def format_info_response(value):
    info = {}
    for line in value.decode('utf-8').splitlines():
        if not line or line[0] == '#':
            continue
        if ':' in line:
            key, value = line.split(':', 1)
            info[key] = parse_info_value(value)
    return info