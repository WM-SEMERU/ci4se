def load_configuration(working_dir):
    import nameset.virtualchain_hooks as virtualchain_hooks
    opts = configure(working_dir)
    blockstack_opts = opts.get('blockstack', None)
    blockstack_api_opts = opts.get('blockstack-api', None)
    bitcoin_opts = opts['bitcoind']
    config_server_version = blockstack_opts.get('server_version', None)
    if config_server_version is None or versions_need_upgrade(
        config_server_version, VERSION):
        print >> sys.stderr, "Obsolete or unrecognizable config file ({}): '{}' != '{}'".format(
            virtualchain.get_config_filename(virtualchain_hooks,
            working_dir), config_server_version, VERSION)
        print >> sys.stderr, 'Please see the release notes for version {} for instructions to upgrade (in the release-notes/ folder).'.format(
            VERSION)
        return None
    set_bitcoin_opts(bitcoin_opts)
    set_blockstack_opts(blockstack_opts)
    set_blockstack_api_opts(blockstack_api_opts)
    return {'bitcoind': bitcoin_opts, 'blockstack': blockstack_opts,
        'blockstack-api': blockstack_api_opts}