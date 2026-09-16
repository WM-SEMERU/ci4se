def version(ruby=None, runas=None, gem_bin=None):
    cmd = ['--version']
    stdout = _gem(cmd, ruby, gem_bin=gem_bin, runas=runas)
    ret = {}
    for line in salt.utils.itertools.split(stdout, '\n'):
        match = re.match('[.0-9]+', line)
        if match:
            ret = line
            break
    return ret