def _do_element_absent(name, elem_type, data, server=None):
    ret = {'delete': False, 'error': None}
    try:
        elements = __salt__['glassfish.enum_{0}'.format(elem_type)]()
    except requests.ConnectionError as error:
        if __opts__['test']:
            ret['create'] = True
            return ret
        else:
            ret['error'] = "Can't connect to the server"
            return ret
    if elements and name in elements:
        ret['delete'] = True
        if not __opts__['test']:
            try:
                __salt__['glassfish.delete_{0}'.format(elem_type)](name,
                    server=server, **data)
            except CommandExecutionError as error:
                ret['error'] = error
    return ret