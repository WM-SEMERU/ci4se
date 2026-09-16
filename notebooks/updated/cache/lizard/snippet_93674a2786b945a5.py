def refresh(name):
    ret = {'name': name, 'changes': {}, 'result': None, 'comment': ''}
    if __opts__['test']:
        ret['comment'] = 'Refreshing local node configuration'
        return ret
    __salt__['trafficserver.refresh']()
    ret['result'] = True
    ret['comment'] = 'Refreshed local node configuration'
    return ret