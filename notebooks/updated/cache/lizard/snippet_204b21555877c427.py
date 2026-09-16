def Main():
    argument_parser = argparse.ArgumentParser(description=
        'Calculates a message digest hash for every file in a directory or storage media image.'
        )
    argument_parser.add_argument('--output_file', '--output-file', dest=
        'output_file', action='store', metavar='source.hashes', default=
        None, help='path of the output file, default is to output to stdout.')
    argument_parser.add_argument('source', nargs='?', action='store',
        metavar='image.raw', default=None, help=
        'path of the directory or storage media image.')
    options = argument_parser.parse_args()
    if not options.source:
        print('Source value is missing.')
        print('')
        argument_parser.print_help()
        print('')
        return False
    logging.basicConfig(level=logging.INFO, format=
        '[%(levelname)s] %(message)s')
    if options.output_file:
        output_writer = FileOutputWriter(options.output_file)
    else:
        output_writer = StdoutWriter()
    try:
        output_writer.Open()
    except IOError as exception:
        print('Unable to open output writer with error: {0!s}.'.format(
            exception))
        print('')
        return False
    return_value = True
    mediator = command_line.CLIVolumeScannerMediator()
    recursive_hasher = RecursiveHasher(mediator=mediator)
    try:
        base_path_specs = recursive_hasher.GetBasePathSpecs(options.source)
        if not base_path_specs:
            print('No supported file system found in source.')
            print('')
            return False
        recursive_hasher.CalculateHashes(base_path_specs, output_writer)
        print('')
        print('Completed.')
    except errors.ScannerError as exception:
        return_value = False
        print('')
        print('[ERROR] {0!s}'.format(exception))
    except errors.UserAbort as exception:
        return_value = False
        print('')
        print('Aborted.')
    output_writer.Close()
    return return_value