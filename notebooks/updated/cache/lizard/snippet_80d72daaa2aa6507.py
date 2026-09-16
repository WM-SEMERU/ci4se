def monitor_key_get(service, key):
    try:
        output = check_output(['ceph', '--id', service, 'config-key', 'get',
            str(key)]).decode('UTF-8')
        return output
    except CalledProcessError as e:
        log('Monitor config-key get failed with message: {}'.format(e.output))
        return None