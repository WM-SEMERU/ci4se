def init(opts):
    proxy_dict = opts.get('proxy', {})
    conn_args = copy.deepcopy(proxy_dict)
    conn_args.pop('proxytype', None)
    opts['multiprocessing'] = conn_args.pop('multiprocessing', True)
    try:
        rpc_reply = __utils__['nxos_api.rpc']('show clock', **conn_args)
        nxos_device['conn_args'] = conn_args
        nxos_device['initialized'] = True
        nxos_device['up'] = True
    except SaltException:
        log.error('Unable to connect to %s', conn_args['host'], exc_info=True)
        raise
    return True