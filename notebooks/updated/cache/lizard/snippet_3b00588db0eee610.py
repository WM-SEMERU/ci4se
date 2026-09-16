def netmiko_multi_call(*methods, **kwargs):
    netmiko_kwargs = netmiko_args()
    kwargs.update(netmiko_kwargs)
    return __salt__['netmiko.multi_call'](*methods, **kwargs)