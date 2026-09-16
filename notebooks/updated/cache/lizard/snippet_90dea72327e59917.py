def sync_all(name, **kwargs):
    ret = {'name': name, 'changes': {}, 'result': True, 'comment': ''}
    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = 'saltutil.sync_all would have been run'
        return ret
    try:
        sync_status = __salt__['saltutil.sync_all'](**kwargs)
        for key, value in sync_status.items():
            if value:
                ret['changes'][key] = value
                ret['comment'] = 'Sync performed'
    except Exception as e:
        log.error('Failed to run saltutil.sync_all: %s', e)
        ret['result'] = False
        ret['comment'] = 'Failed to run sync_all: {0}'.format(e)
        return ret
    if not ret['changes']:
        ret['comment'] = 'No updates to sync'
    return ret