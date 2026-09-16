def parse_args(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(description=
        'MicroDrop plugin Conda recipe builder')
    parser.add_argument('-s', '--source-dir', type=ph.path, nargs='?')
    parser.add_argument('-t', '--target-dir', type=ph.path, nargs='?')
    parser.add_argument('-p', '--package-name', nargs='?')
    parser.add_argument('-V', '--version-number', nargs='?')
    parsed_args = parser.parse_args()
    if not parsed_args.source_dir:
        parsed_args.source_dir = ph.path(os.environ['SRC_DIR'])
    if not parsed_args.target_dir:
        prefix_dir = ph.path(os.environ['PREFIX'])
        module_name = os.environ['PKG_NAME'].split('.')[-1].replace('-', '_')
        parsed_args.target_dir = prefix_dir.joinpath('share', 'microdrop',
            'plugins', 'available', module_name)
    if not parsed_args.package_name:
        parsed_args.package_name = os.environ['PKG_NAME']
    return parsed_args