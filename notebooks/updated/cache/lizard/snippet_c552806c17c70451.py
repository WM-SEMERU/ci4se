def delete_launch_configuration(name, region=None, key=None, keyid=None,
    profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    retries = 30
    while True:
        try:
            conn.delete_launch_configuration(name)
            log.info('Deleted LC %s', name)
            return True
        except boto.exception.BotoServerError as e:
            if retries and e.code == 'Throttling':
                log.debug('Throttled by AWS API, retrying in 5 seconds...')
                time.sleep(5)
                retries -= 1
                continue
            log.error(e)
            msg = 'Failed to delete LC {0}'.format(name)
            log.error(msg)
            return False