def is_stable_version(version):
    if not isinstance(version, tuple):
        version = version.split('.')
    last_part = version[-1]
    if not re.search('[a-zA-Z]', last_part):
        return True
    else:
        return False