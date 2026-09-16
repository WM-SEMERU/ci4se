def configmap_absent(name, namespace='default', **kwargs):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}
    configmap = __salt__['kubernetes.show_configmap'](name, namespace, **kwargs
        )
    if configmap is None:
        ret['result'] = True if not __opts__['test'] else None
        ret['comment'] = 'The configmap does not exist'
        return ret
    if __opts__['test']:
        ret['comment'] = 'The configmap is going to be deleted'
        ret['result'] = None
        return ret
    __salt__['kubernetes.delete_configmap'](name, namespace, **kwargs)
    ret['result'] = True
    ret['changes'] = {'kubernetes.configmap': {'new': 'absent', 'old':
        'present'}}
    ret['comment'] = 'ConfigMap deleted'
    return ret