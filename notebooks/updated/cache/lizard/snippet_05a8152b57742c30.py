def _parse_env_var_file(data):
    output = {}
    for line in data.splitlines():
        line = line.strip()
        if not line or '=' not in line:
            continue
        parts = line.split('=')
        if len(parts) != 2:
            continue
        name = parts[0]
        value = parts[1]
        if len(value) > 1:
            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1]
        output[name] = value
    return output