def status(cwd, opts=None, user=None):

    def _status(cwd):
        cmd = ['hg', 'status']
        if opts:
            for opt in opts.split():
                cmd.append('{0}'.format(opt))
        out = __salt__['cmd.run_stdout'](cmd, cwd=cwd, runas=user,
            python_shell=False)
        types = {'M': 'modified', 'A': 'added', 'R': 'removed', 'C':
            'clean', '!': 'missing', '?': 'not tracked', 'I': 'ignored',
            ' ': 'origin of the previous file'}
        ret = {}
        for line in out.splitlines():
            t, f = types[line[0]], line[2:]
            if t not in ret:
                ret[t] = []
            ret[t].append(f)
        return ret
    if salt.utils.data.is_iter(cwd):
        return dict((cwd, _status(cwd)) for cwd in cwd)
    else:
        return _status(cwd)