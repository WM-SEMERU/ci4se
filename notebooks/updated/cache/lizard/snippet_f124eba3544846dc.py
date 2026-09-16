def add_key(service, key):
    keyring = _keyring_path(service)
    if os.path.exists(keyring):
        with open(keyring, 'r') as ring:
            if key in ring.read():
                log('Ceph keyring exists at %s and has not changed.' %
                    keyring, level=DEBUG)
                return
            log('Updating existing keyring %s.' % keyring, level=DEBUG)
    cmd = ['ceph-authtool', keyring, '--create-keyring', '--name=client.{}'
        .format(service), '--add-key={}'.format(key)]
    check_call(cmd)
    log('Created new ceph keyring at %s.' % keyring, level=DEBUG)