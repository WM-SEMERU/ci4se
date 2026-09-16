def ssh_key(key):
    value = str(key)
    if not os.path.isfile(value):
        raise Exception('File Does not Exist: %s' % key)
    return value