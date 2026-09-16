def _prepare_connection(**kwargs):
    init_args = {}
    fun_kwargs = {}
    netmiko_kwargs = __salt__['config.get']('netmiko', {})
    netmiko_kwargs.update(kwargs)
    netmiko_init_args, _, _, netmiko_defaults = inspect.getargspec(
        BaseConnection.__init__)
    check_self = netmiko_init_args.pop(0)
    for karg, warg in six.iteritems(netmiko_kwargs):
        if karg not in netmiko_init_args:
            if warg is not None:
                fun_kwargs[karg] = warg
            continue
        if warg is not None:
            init_args[karg] = warg
    conn = ConnectHandler(**init_args)
    return conn, fun_kwargs