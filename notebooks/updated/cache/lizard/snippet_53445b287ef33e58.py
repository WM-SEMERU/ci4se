def create_node(hostname, username, password, name, address):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}
    if __opts__['test']:
        return _test_output(ret, 'create', params={'hostname': hostname,
            'username': username, 'password': password, 'name': name,
            'address': address})
    existing = __salt__['bigip.list_node'](hostname, username, password, name)
    if existing['code'] == 200:
        ret['result'] = True
        ret['comment'
            ] = 'A node by this name currently exists.  No change made.'
    elif existing['code'] == 404:
        response = __salt__['bigip.create_node'](hostname, username,
            password, name, address)
        ret['result'] = True
        ret['changes']['old'] = {}
        ret['changes']['new'] = response['content']
        ret['comment'] = 'Node was successfully created.'
    else:
        ret = _load_result(existing, ret)
    return ret