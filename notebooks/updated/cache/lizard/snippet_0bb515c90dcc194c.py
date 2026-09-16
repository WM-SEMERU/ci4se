def swapon(name, priority=None):
    ret = {}
    on_ = swaps()
    if name in on_:
        ret['stats'] = on_[name]
        ret['new'] = False
        return ret
    if __grains__['kernel'] == 'SunOS':
        if __grains__['virtual'] != 'zone':
            __salt__['cmd.run']('swap -a {0}'.format(name), python_shell=False)
        else:
            return False
    else:
        cmd = 'swapon {0}'.format(name)
        if priority and 'AIX' not in __grains__['kernel']:
            cmd += ' -p {0}'.format(priority)
        __salt__['cmd.run'](cmd, python_shell=False)
    on_ = swaps()
    if name in on_:
        ret['stats'] = on_[name]
        ret['new'] = True
        return ret
    return ret