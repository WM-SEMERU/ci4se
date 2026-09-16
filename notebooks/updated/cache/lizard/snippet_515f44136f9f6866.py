def absent(name, protocol=None, service_address=None, server_address=None):
    ret = {'name': name, 'changes': {}, 'result': True, 'comment': ''}
    server_check = __salt__['lvs.check_server'](protocol=protocol,
        service_address=service_address, server_address=server_address)
    if server_check is True:
        if __opts__['test']:
            ret['result'] = None
            ret['comment'] = (
                'LVS Server {0} in service {1}({2}) is present and needs to be removed'
                .format(name, service_address, protocol))
            return ret
        server_delete = __salt__['lvs.delete_server'](protocol=protocol,
            service_address=service_address, server_address=server_address)
        if server_delete is True:
            ret['comment'
                ] = 'LVS Server {0} in service {1}({2}) has been removed'.format(
                name, service_address, protocol)
            ret['changes'][name] = 'Absent'
            return ret
        else:
            ret['comment'] = (
                'LVS Server {0} in service {1}({2}) removed failed({3})'.
                format(name, service_address, protocol, server_delete))
            ret['result'] = False
            return ret
    else:
        ret['comment'] = (
            'LVS Server {0} in service {1}({2}) is not present, so it cannot be removed'
            .format(name, service_address, protocol))
    return ret