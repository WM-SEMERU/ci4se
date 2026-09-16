def deployment_absent(name, namespace='default', **kwargs):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}
    deployment = __salt__['kubernetes.show_deployment'](name, namespace, **
        kwargs)
    if deployment is None:
        ret['result'] = True if not __opts__['test'] else None
        ret['comment'] = 'The deployment does not exist'
        return ret
    if __opts__['test']:
        ret['comment'] = 'The deployment is going to be deleted'
        ret['result'] = None
        return ret
    res = __salt__['kubernetes.delete_deployment'](name, namespace, **kwargs)
    if res['code'] == 200:
        ret['result'] = True
        ret['changes'] = {'kubernetes.deployment': {'new': 'absent', 'old':
            'present'}}
        ret['comment'] = res['message']
    else:
        ret['comment'] = 'Something went wrong, response: {0}'.format(res)
    return ret