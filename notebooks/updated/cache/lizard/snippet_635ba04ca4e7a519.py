def absent(name, service_name, auth=None, **kwargs):
    ret = {'name': name, 'changes': {}, 'result': True, 'comment': ''}
    __salt__['keystoneng.setup_clouds'](auth)
    success, val = _, endpoint = _common(ret, name, service_name, kwargs)
    if not success:
        return val
    if endpoint:
        if __opts__['test'] is True:
            ret['result'] = None
            ret['changes'] = {'id': endpoint.id}
            ret['comment'] = 'Endpoint will be deleted.'
            return ret
        __salt__['keystoneng.endpoint_delete'](id=endpoint.id)
        ret['changes']['id'] = endpoint.id
        ret['comment'] = 'Deleted endpoint'
    return ret