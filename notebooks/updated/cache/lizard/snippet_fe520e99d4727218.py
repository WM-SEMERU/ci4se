def read_config(config_path):
    result = {}
    with open(config_path, 'r') as fd:
        for line in fd.readlines():
            if '=' in line:
                key, value = line.split('=', 1)
                try:
                    result[key] = json.loads(value)
                except ValueError:
                    result[key] = value.rstrip('\n')
    return result