def configmap_present(name, namespace='default', data=None, source=None,
    template=None, **kwargs):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}
    if data and source:
        return _error(ret, "'source' cannot be used in combination with 'data'"
            )
    elif data is None:
        data = {}
    configmap = __salt__['kubernetes.show_configmap'](name, namespace, **kwargs
        )
    if configmap is None:
        if __opts__['test']:
            ret['result'] = None
            ret['comment'] = 'The configmap is going to be created'
            return ret
        res = __salt__['kubernetes.create_configmap'](name=name, namespace=
            namespace, data=data, source=source, template=template, saltenv
            =__env__, **kwargs)
        ret['changes']['{0}.{1}'.format(namespace, name)] = {'old': {},
            'new': res}
    else:
        if __opts__['test']:
            ret['result'] = None
            ret['comment'] = 'The configmap is going to be replaced'
            return ret
        log.info('Forcing the recreation of the service')
        ret['comment'] = 'The configmap is already present. Forcing recreation'
        res = __salt__['kubernetes.replace_configmap'](name=name, namespace
            =namespace, data=data, source=source, template=template,
            saltenv=__env__, **kwargs)
    ret['changes'] = {'data': res['data']}
    ret['result'] = True
    return ret