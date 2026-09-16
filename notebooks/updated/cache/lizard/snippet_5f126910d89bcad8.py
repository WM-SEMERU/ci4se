def absent(name, poll=5, timeout=60, profile=None):
    log.debug('Absent with (%s, %s %s)', name, poll, profile)
    ret = {'name': None, 'comment': '', 'changes': {}, 'result': True}
    if not name:
        ret['result'] = False
        ret['comment'] = 'Name ist not valid'
        return ret
    ret['name'] = name,
    existing_stack = __salt__['heat.show_stack'](name, profile=profile)
    if not existing_stack['result']:
        ret['result'] = True
        ret['comment'] = 'Stack not exist'
        return ret
    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = 'Stack {0} is set to be removed'.format(name)
        return ret
    stack = __salt__['heat.delete_stack'](name=name, poll=poll, timeout=
        timeout, profile=profile)
    ret['result'] = stack['result']
    ret['comment'] = stack['comment']
    ret['changes']['stack_name'] = name
    ret['changes']['comment'] = 'Delete stack'
    return ret