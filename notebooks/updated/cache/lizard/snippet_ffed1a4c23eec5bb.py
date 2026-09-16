def purge(name, delete_key=True):
    ret = {}
    client = salt.client.get_local_client(__opts__['conf_file'])
    data = vm_info(name, quiet=True)
    if not data:
        __jid_event__.fire_event({'error': 'Failed to find VM {0} to purge'
            .format(name)}, 'progress')
        return 'fail'
    host = next(six.iterkeys(data))
    try:
        cmd_ret = client.cmd_iter(host, 'virt.purge', [name, True], timeout=600
            )
    except SaltClientError as client_error:
        return 'Virtual machine {0} could not be purged: {1}'.format(name,
            client_error)
    for comp in cmd_ret:
        ret.update(comp)
    if delete_key:
        log.debug('Deleting key %s', name)
        skey = salt.key.Key(__opts__)
        skey.delete_key(name)
    __jid_event__.fire_event({'message': 'Purged VM {0}'.format(name)},
        'progress')
    return 'good'