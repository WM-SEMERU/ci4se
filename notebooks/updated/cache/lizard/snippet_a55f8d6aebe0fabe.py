def module_remove(name):
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}
    modules = __salt__['selinux.list_semod']()
    if name not in modules:
        ret['comment'] = 'Module {0} is not available'.format(name)
        ret['result'] = False
        return ret
    if __salt__['selinux.remove_semod'](name):
        ret['comment'] = 'Module {0} has been removed'.format(name)
        return ret
    ret['result'] = False
    ret['comment'] = 'Failed to remove module {0}'.format(name)
    return ret