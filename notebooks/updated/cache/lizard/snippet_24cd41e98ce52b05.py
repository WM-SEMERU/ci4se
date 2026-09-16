def port(name, private_port=None):
    pattern_used = bool(re.search('[*?\\[]', name))
    names = fnmatch.filter(list_containers(all=True), name
        ) if pattern_used else [name]
    if private_port is None:
        pattern = '*'
    elif isinstance(private_port, six.integer_types):
        pattern = '{0}/*'.format(private_port)
    else:
        err = (
            "Invalid private_port '{0}'. Must either be a port number, or be in port/protocol notation (e.g. 5000/tcp)"
            .format(private_port))
        try:
            port_num, _, protocol = private_port.partition('/')
            protocol = protocol.lower()
            if not port_num.isdigit() or protocol not in ('tcp', 'udp'):
                raise SaltInvocationError(err)
            pattern = port_num + '/' + protocol
        except AttributeError:
            raise SaltInvocationError(err)
    ret = {}
    for c_name in names:
        mappings = inspect_container(c_name).get('NetworkSettings', {}).get(
            'Ports', {})
        ret[c_name] = dict((x, mappings[x]) for x in fnmatch.filter(
            mappings, pattern))
    return ret.get(name, {}) if not pattern_used else ret