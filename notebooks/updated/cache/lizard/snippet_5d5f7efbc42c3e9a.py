def get_secgroup_id(kwargs=None, call=None):
    if call == 'action':
        raise SaltCloudSystemExit(
            'The get_secgroup_id function must be called with -f or --function.'
            )
    if kwargs is None:
        kwargs = {}
    name = kwargs.get('name', None)
    if name is None:
        raise SaltCloudSystemExit(
            "The get_secgroup_id function requires a 'name'.")
    try:
        ret = list_security_groups()[name]['id']
    except KeyError:
        raise SaltCloudSystemExit(
            "The security group '{0}' could not be found.".format(name))
    return ret