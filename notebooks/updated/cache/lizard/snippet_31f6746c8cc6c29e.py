def enable(states):
    ret = {'res': True, 'msg': ''}
    states = salt.utils.args.split_input(states)
    log.debug('states %s', states)
    msg = []
    _disabled = __salt__['grains.get']('state_runs_disabled')
    if not isinstance(_disabled, list):
        _disabled = []
    _changed = False
    for _state in states:
        log.debug('_state %s', _state)
        if _state not in _disabled:
            msg.append('Info: {0} state already enabled.'.format(_state))
        else:
            msg.append('Info: {0} state enabled.'.format(_state))
            _disabled.remove(_state)
            _changed = True
    if _changed:
        __salt__['grains.setval']('state_runs_disabled', _disabled)
    ret['msg'] = '\n'.join(msg)
    __salt__['saltutil.refresh_modules']()
    return ret