def run():
    args = parse_args()
    logging.basicConfig(level=logging.WARN)
    logging.getLogger('kafka').setLevel(logging.CRITICAL)
    if args.controller_only and args.first_broker_only:
        terminate(status_code.WARNING, prepare_terminate_message(
            'Only one of controller_only and first_broker_only should be used'
            ), args.json)
    if args.controller_only or args.first_broker_only:
        if args.broker_id is None:
            terminate(status_code.WARNING, prepare_terminate_message(
                'broker_id is not specified'), args.json)
        elif args.broker_id == -1:
            try:
                args.broker_id = get_broker_id(args.data_path)
            except Exception as e:
                terminate(status_code.WARNING, prepare_terminate_message(
                    '{}'.format(e)), args.json)
    try:
        cluster_config = config.get_cluster_config(args.cluster_type, args.
            cluster_name, args.discovery_base_path)
        code, msg = args.command(cluster_config, args)
    except ConfigurationError as e:
        terminate(status_code.CRITICAL, prepare_terminate_message(
            'ConfigurationError {0}'.format(e)), args.json)
    terminate(code, msg, args.json)