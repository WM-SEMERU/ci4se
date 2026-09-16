def status(name, sig=None):
    cmd = 's6-svstat {0}'.format(_service_path(name))
    out = __salt__['cmd.run_stdout'](cmd)
    try:
        pid = re.search('up \\(pid (\\d+)\\)', out).group(1)
    except AttributeError:
        pid = ''
    return pid