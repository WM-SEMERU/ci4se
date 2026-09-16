def agent_service_deregister(consul_url=None, token=None, serviceid=None):
    ret = {}
    data = {}
    if not consul_url:
        consul_url = _get_config()
        if not consul_url:
            log.error('No Consul URL found.')
            ret['message'] = 'No Consul URL found.'
            ret['res'] = False
            return ret
    if not serviceid:
        raise SaltInvocationError('Required argument "serviceid" is missing.')
    function = 'agent/service/deregister/{0}'.format(serviceid)
    res = _query(consul_url=consul_url, function=function, token=token,
        method='PUT', data=data)
    if res['res']:
        ret['res'] = True
        ret['message'] = 'Service {0} removed from agent.'.format(serviceid)
    else:
        ret['res'] = False
        ret['message'] = 'Unable to remove service {0}.'.format(serviceid)
    return ret