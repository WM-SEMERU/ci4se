def read_file_values(env_file, fail_silently=True):
    env_data = {}
    try:
        with open(env_file) as f:
            content = f.read()
    except IOError:
        if fail_silently:
            logging.error("Could not read file '{0}'".format(env_file))
            return env_data
        raise
    for line in content.splitlines():
        m1 = re.match('\\A([A-Za-z_0-9]+)=(.*)\\Z', line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match("\\A'(.*)'\\Z", val)
            if m2:
                val = m2.group(1)
            m3 = re.match('\\A"(.*)"\\Z', val)
            if m3:
                val = re.sub('\\\\(.)', '\\1', m3.group(1))
            env_data[key] = val
    return env_data