def _get_netmiko_args(optional_args):
    if HAS_NETMIKO_HELPERS:
        return napalm.base.netmiko_helpers.netmiko_args(optional_args)
    netmiko_args, _, _, netmiko_defaults = inspect.getargspec(BaseConnection
        .__init__)
    check_self = netmiko_args.pop(0)
    if check_self != 'self':
        raise ValueError('Error processing Netmiko arguments')
    netmiko_argument_map = dict(six.moves.zip(netmiko_args, netmiko_defaults))
    netmiko_filter = ['ip', 'host', 'username', 'password', 'device_type',
        'timeout']
    for k in netmiko_filter:
        netmiko_argument_map.pop(k)
    netmiko_optional_args = {}
    for k, v in six.iteritems(netmiko_argument_map):
        try:
            netmiko_optional_args[k] = optional_args[k]
        except KeyError:
            pass
    return netmiko_optional_args