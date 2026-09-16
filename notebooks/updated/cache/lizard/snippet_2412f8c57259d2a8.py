def source_present(name, source_type='imgapi'):
    ret = {'name': name, 'changes': {}, 'result': None, 'comment': ''}
    if name in __salt__['imgadm.sources']():
        ret['result'] = True
        ret['comment'] = 'image source {0} is present'.format(name)
    else:
        if __opts__['test']:
            res = {}
            ret['result'] = True
        else:
            res = __salt__['imgadm.source_add'](name, source_type)
            ret['result'] = name in res
        if ret['result']:
            ret['comment'] = 'image source {0} added'.format(name)
            ret['changes'][name] = 'added'
        else:
            ret['comment'] = 'image source {0} not added'.format(name)
            if 'Error' in res:
                ret['comment'] = '{0}: {1}'.format(ret['comment'], res['Error']
                    )
    return ret