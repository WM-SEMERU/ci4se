def get_config(base_dir=''):
    p = configargparse.ArgParser(description=
        'IIIF Image API Reference Service', default_config_files=[os.path.
        join(base_dir, 'iiif_reference_server.cfg')], formatter_class=
        configargparse.ArgumentDefaultsHelpFormatter)
    add_shared_configs(p, base_dir)
    p.add('--scale-factors', default='auto', help=
        "Set of tile scale factors or 'auto' to calculate for each image such that there are tiles up to the full image"
        )
    p.add('--api-versions', default='1.0,1.1,2.0,2.1', help=
        'Set of API versions to support')
    args = p.parse_args()
    if args.debug:
        args.verbose = True
    elif args.verbose:
        args.quiet = False
    args.scale_factors = split_comma_argument(args.scale_factors)
    args.api_versions = split_comma_argument(args.api_versions)
    logging_level = logging.WARNING
    if args.verbose:
        logging_level = logging.INFO
    elif args.quiet:
        logging_level = logging.ERROR
    logging.basicConfig(format='%(name)s: %(message)s', level=logging_level)
    return args