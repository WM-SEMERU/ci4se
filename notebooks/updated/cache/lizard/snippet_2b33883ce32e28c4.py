def mode(name):
    ret = {'name': name, 'result': False, 'comment': '', 'changes': {}}
    tmode = _refine_mode(name)
    if tmode == 'unknown':
        ret['comment'] = '{0} is not an accepted mode'.format(name)
        return ret
    mode = __salt__['selinux.getenforce']()
    config = __salt__['selinux.getconfig']()
    if mode == tmode and mode != config and tmode != config:
        mode = config
    if mode == tmode:
        ret['result'] = True
        ret['comment'] = 'SELinux is already in {0} mode'.format(tmode)
        return ret
    if __opts__['test']:
        ret['comment'] = 'SELinux mode is set to be changed to {0}'.format(
            tmode)
        ret['result'] = None
        ret['changes'] = {'old': mode, 'new': tmode}
        return ret
    oldmode, mode = mode, __salt__['selinux.setenforce'](tmode)
    if mode == tmode or tmode == 'Disabled' and __salt__['selinux.getconfig'](
        ) == tmode:
        ret['result'] = True
        ret['comment'] = 'SELinux has been set to {0} mode'.format(tmode)
        ret['changes'] = {'old': oldmode, 'new': mode}
        return ret
    ret['comment'] = 'Failed to set SELinux to {0} mode'.format(tmode)
    return ret