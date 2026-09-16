def get_conf(path, fatal=True, keep_empty=False, default=None):
    if not path:
        return default
    lines = path if isinstance(path, list) else get_lines(path, fatal=fatal,
        default=default)
    result = default
    if lines is not None:
        result = {}
        section_key = None
        section = None
        for line in lines:
            line = decode(line).strip()
            if '#' in line:
                i = line.index('#')
                line = line[:i].strip()
            if not line:
                continue
            if line.startswith('[') and line.endswith(']'):
                section_key = line.strip('[]').strip()
                section = result.get(section_key)
                continue
            if '=' not in line:
                continue
            if section is None:
                section = result[section_key] = {}
            key, _, value = line.partition('=')
            key = key.strip()
            value = value.strip()
            if keep_empty or key and value:
                section[key] = value
        if not keep_empty:
            result = dict((k, v) for k, v in result.items() if k and v)
    return result