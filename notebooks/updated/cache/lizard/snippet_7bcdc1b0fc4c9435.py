def trigger_event(name, event, value1=None, value2=None, value3=None):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}
    if __opts__['test']:
        ret['comment'
            ] = 'The following trigger would be sent to IFTTT: {0}'.format(
            event)
        ret['result'] = None
        return ret
    ret['result'] = __salt__['ifttt.trigger_event'](event=event, value1=
        value1, value2=value2, value3=value3)
    if ret and ret['result']:
        ret['result'] = True
        ret['comment'] = 'Triggered Event: {0}'.format(name)
    else:
        ret['comment'] = 'Failed to trigger event: {0}'.format(name)
    return ret