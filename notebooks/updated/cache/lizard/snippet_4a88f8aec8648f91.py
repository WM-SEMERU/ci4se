def add_haproxy_checks(nrpe, unit_name):
    nrpe.add_check(shortname='haproxy_servers', description=
        'Check HAProxy {%s}' % unit_name, check_cmd='check_haproxy.sh')
    nrpe.add_check(shortname='haproxy_queue', description=
        'Check HAProxy queue depth {%s}' % unit_name, check_cmd=
        'check_haproxy_queue_depth.sh')