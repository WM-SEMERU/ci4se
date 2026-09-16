def rsync(config_file, source, target, override_cluster_name, down):
    config = yaml.load(open(config_file).read())
    if override_cluster_name is not None:
        config['cluster_name'] = override_cluster_name
    config = _bootstrap_config(config)
    head_node = _get_head_node(config, config_file, override_cluster_name,
        create_if_needed=False)
    provider = get_node_provider(config['provider'], config['cluster_name'])
    try:
        updater = NodeUpdaterThread(node_id=head_node, provider_config=
            config['provider'], provider=provider, auth_config=config[
            'auth'], cluster_name=config['cluster_name'], file_mounts=
            config['file_mounts'], initialization_commands=[],
            setup_commands=[], runtime_hash='')
        if down:
            rsync = updater.rsync_down
        else:
            rsync = updater.rsync_up
        rsync(source, target, check_error=False)
    finally:
        provider.cleanup()