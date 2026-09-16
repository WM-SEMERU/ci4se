def login_failures(user):
    cmd = 'lsuser -a unsuccessful_login_count {0}'.format(user)
    cmd += " | grep -E 'unsuccessful_login_count=([3-9]|[0-9][0-9]+)'"
    out = __salt__['cmd.run_all'](cmd, output_loglevel='trace',
        python_shell=True)
    ret = []
    lines = out['stdout'].splitlines()
    for line in lines:
        ret.append(line.split()[0])
    return ret