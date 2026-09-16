def status(name, sig=None):
    contains_globbing = bool(re.search('\\*|\\?|\\[.+\\]', name))
    if contains_globbing:
        services = fnmatch.filter(get_all(), name)
    else:
        services = [name]
    results = {}
    for service in services:
        cmd = '/usr/bin/svcs -H -o STATE {0}'.format(service)
        line = __salt__['cmd.run'](cmd, python_shell=False)
        results[service] = line == 'online'
    if contains_globbing:
        return results
    return results[name]