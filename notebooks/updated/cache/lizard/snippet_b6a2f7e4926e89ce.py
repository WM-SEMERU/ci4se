def get_instance_id():
    log = logging.getLogger(mod_logger + '.get_instance_id')
    if not is_aws():
        log.info('This machine is not running in AWS, exiting...')
        return
    instance_id_url = metadata_url + 'instance-id'
    try:
        response = urllib.urlopen(instance_id_url)
    except (IOError, OSError) as ex:
        msg = 'Unable to query URL to get instance ID: {u}\n{e}'.format(u=
            instance_id_url, e=ex)
        log.error(msg)
        return
    if response.getcode() != 200:
        msg = (
            'There was a problem querying url: {u}, returned code: {c}, unable to get the instance-id'
            .format(u=instance_id_url, c=response.getcode()))
        log.error(msg)
        return
    instance_id = response.read()
    return instance_id