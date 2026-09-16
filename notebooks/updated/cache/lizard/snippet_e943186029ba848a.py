def list_clusters(kwargs=None, call=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The list_clusters function must be called with -f or --function.')
    return {'Clusters': salt.utils.vmware.list_clusters(_get_si())}