def acl_info(consul_url=None, **kwargs):
    ret = {}
    data = {}
    if not consul_url:
        consul_url = _get_config()
        if not consul_url:
            log.error('No Consul URL found.')
            ret['message'] = 'No Consul URL found.'
            ret['res'] = False
            return ret
    if 'id' not in kwargs:
        ret['message'] = 'Required parameter "id" is missing.'
        ret['res'] = False
        return ret
    function = 'acl/info/{0}'.format(kwargs['id'])
    ret = _query(consul_url=consul_url, data=data, method='GET', function=
        function)
    return ret