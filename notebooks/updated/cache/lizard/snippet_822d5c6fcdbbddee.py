def cli(env, **args):
    create_args = _parse_create_args(env.client, args)
    create_args['primary_disk'] = args.get('primary_disk')
    manager = CapacityManager(env.client)
    capacity_id = args.get('capacity_id')
    test = args.get('test')
    result = manager.create_guest(capacity_id, test, create_args)
    env.fout(_build_receipt(result, test))