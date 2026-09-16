def boolean(name, value, persist=False):
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}
    bools = __salt__['selinux.list_sebool']()
    if name not in bools:
        ret['comment'] = 'Boolean {0} is not available'.format(name)
        ret['result'] = False
        return ret
    rvalue = _refine_value(value)
    if rvalue is None:
        ret['comment'] = '{0} is not a valid value for the boolean'.format(
            value)
        ret['result'] = False
        return ret
    state = bools[name]['State'] == rvalue
    default = bools[name]['Default'] == rvalue
    if persist:
        if state and default:
            ret['comment'] = 'Boolean is in the correct state'
            return ret
    elif state:
        ret['comment'] = 'Boolean is in the correct state'
        return ret
    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = 'Boolean {0} is set to be changed to {1}'.format(name,
            rvalue)
        return ret
    ret['result'] = __salt__['selinux.setsebool'](name, rvalue, persist)
    if ret['result']:
        ret['comment'] = 'Boolean {0} has been set to {1}'.format(name, rvalue)
        ret['changes'].update({'State': {'old': bools[name]['State'], 'new':
            rvalue}})
        if persist and not default:
            ret['changes'].update({'Default': {'old': bools[name]['Default'
                ], 'new': rvalue}})
        return ret
    ret['comment'] = 'Failed to set the boolean {0} to {1}'.format(name, rvalue
        )
    return ret