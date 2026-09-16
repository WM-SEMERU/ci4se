def run_analysis(self, argv):
    args = self._parser.parse_args(argv)
    if is_null(args.config):
        raise ValueError('Config yaml file must be specified')
    if is_null(args.rand_config):
        raise ValueError('Random direction config yaml file must be specified')
    config = load_yaml(args.config)
    rand_config = load_yaml(args.rand_config)
    wcsgeom = self._make_wcsgeom_from_config(config)
    dir_dict = self._build_skydir_dict(wcsgeom, rand_config)
    if is_not_null(args.outfile):
        write_yaml(dir_dict, args.outfile)