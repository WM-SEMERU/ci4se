def get_vcenter_version(kwargs=None, call=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The get_vcenter_version function must be called with -f or --function.'
            )
    inv = salt.utils.vmware.get_inventory(_get_si())
    return inv.about.fullName