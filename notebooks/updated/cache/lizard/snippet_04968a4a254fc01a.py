def network_manager():
    release = os_release('nova-common')
    manager = config('network-manager').lower()
    if manager not in ['quantum', 'neutron']:
        return manager
    if release in ['essex']:
        log('Neutron networking not supported in Essex.', level=ERROR)
        raise Exception
    elif release in ['folsom', 'grizzly']:
        return 'quantum'
    else:
        return 'neutron'