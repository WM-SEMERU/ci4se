def acl_list(consul_url=None, token=None, **kwargs):
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
    function = 'acl/list'
    ret = _query(consul_url=consul_url, token=token, data=data, method=
        'PUT', function=function)
    return ret