def teardown_cluster(config_file, yes, workers_only, override_cluster_name):
    config = yaml.load(open(config_file).read())
    if override_cluster_name is not None:
        config['cluster_name'] = override_cluster_name
    validate_config(config)
    config = fillout_defaults(config)
    confirm('This will destroy your cluster', yes)
    provider = get_node_provider(config['provider'], config['cluster_name'])
    try:

        def remaining_nodes():
            if workers_only:
                A = []
            else:
                A = [node_id for node_id in provider.non_terminated_nodes({
                    TAG_RAY_NODE_TYPE: 'head'})]
            A += [node_id for node_id in provider.non_terminated_nodes({
                TAG_RAY_NODE_TYPE: 'worker'})]
            return A
        A = remaining_nodes()
        with LogTimer('teardown_cluster: Termination done.'):
            while A:
                logger.info('teardown_cluster: Terminating {} nodes...'.
                    format(len(A)))
                provider.terminate_nodes(A)
                time.sleep(1)
                A = remaining_nodes()
    finally:
        provider.cleanup()