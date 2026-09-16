def list_networks(kwargs=None, call=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The list_networks function must be called with -f or --function.')
    return {'Networks': salt.utils.vmware.list_networks(_get_si())}