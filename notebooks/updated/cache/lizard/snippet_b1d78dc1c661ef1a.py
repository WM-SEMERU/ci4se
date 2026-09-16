def get_mon_map(service):
    try:
        mon_status = check_output(['ceph', '--id', service, 'mon_status',
            '--format=json'])
        if six.PY3:
            mon_status = mon_status.decode('UTF-8')
        try:
            return json.loads(mon_status)
        except ValueError as v:
            log('Unable to parse mon_status json: {}. Error: {}'.format(
                mon_status, str(v)))
            raise
    except CalledProcessError as e:
        log('mon_status command failed with message: {}'.format(str(e)))
        raise