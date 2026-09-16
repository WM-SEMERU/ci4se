def do_genesis(args, data_dir=None):
    if data_dir is None:
        data_dir = get_data_dir()
    if not os.path.exists(data_dir):
        raise CliException('Data directory does not exist: {}'.format(data_dir)
            )
    genesis_batches = []
    for input_file in args.input_file:
        print('Processing {}...'.format(input_file))
        input_data = BatchList()
        try:
            with open(input_file, 'rb') as in_file:
                input_data.ParseFromString(in_file.read())
        except:
            raise CliException('Unable to read {}'.format(input_file))
        genesis_batches += input_data.batches
    _validate_depedencies(genesis_batches)
    _check_required_settings(genesis_batches)
    if args.output:
        genesis_file = args.output
    else:
        genesis_file = os.path.join(data_dir, 'genesis.batch')
    print('Generating {}'.format(genesis_file))
    output_data = GenesisData(batches=genesis_batches)
    with open(genesis_file, 'wb') as out_file:
        out_file.write(output_data.SerializeToString())