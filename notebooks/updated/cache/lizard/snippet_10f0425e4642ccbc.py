def describe(cwd, rev='tip', user=None):
    cmd = ['hg', 'log', '-r', '{0}'.format(rev), '--template',
        "'{{latesttag}}-{{latesttagdistance}}-{{node|short}}'"]
    desc = __salt__['cmd.run_stdout'](cmd, cwd=cwd, runas=user,
        python_shell=False)
    return desc or revision(cwd, rev, short=True)