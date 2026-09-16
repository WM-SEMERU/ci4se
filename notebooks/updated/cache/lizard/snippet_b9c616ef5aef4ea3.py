def agent_self(consul_url=None, token=None):
    ret = {}
    query_params = {}
    if not consul_url:
        consul_url = _get_config()
        if not consul_url:
            log.error('No Consul URL found.')
            ret['message'] = 'No Consul URL found.'
            ret['res'] = False
            return ret
    function = 'agent/self'
    ret = _query(consul_url=consul_url, function=function, token=token,
        method='GET', query_params=query_params)
    return ret