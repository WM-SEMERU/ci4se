def get_ip_prefixes_from_bird(filename):
    prefixes = []
    with open(filename, 'r') as bird_conf:
        lines = bird_conf.read()
    for line in lines.splitlines():
        line = line.strip(', ')
        if valid_ip_prefix(line):
            prefixes.append(line)
    return prefixes