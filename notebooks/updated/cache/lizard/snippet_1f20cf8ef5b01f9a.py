def health_state(consul_url=None, token=None, state=None, **kwargs):
    ret = {}
    query_params = {}
    if not consul_url:
        consul_url = _get_config()
        if not consul_url:
            log.error('No Consul URL found.')
            ret['message'] = 'No Consul URL found.'
            ret['res'] = False
            return ret
    if not state:
        raise SaltInvocationError('Required argument "state" is missing.')
    if 'dc' in kwargs:
        query_params['dc'] = kwargs['dc']
    if state not in ('any', 'unknown', 'passing', 'warning', 'critical'):
        ret['message'
            ] = 'State must be any, unknown, passing, warning, or critical.'
        ret['res'] = False
        return ret
    function = 'health/state/{0}'.format(state)
    ret = _query(consul_url=consul_url, function=function, token=token,
        query_params=query_params)
    return ret