def build_parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-o', '--output', help=
        'The output file to save.  If multiple files are generated this is the output prefix for them all.'
        )
    parser.add_argument('-f', '--format', default='json', choices=[
        'c_files', 'command_map_c', 'command_map_h', 'config_map_c',
        'config_map_h', 'json'], type=str, help=
        'the output format for the compiled result.')
    parser.add_argument('bus_definition', nargs='+', help=
        'One or more tilebus definition files to compile')
    return parser