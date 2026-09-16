def get_configs(args, command_args, ansible_args=()):
    configs = [config.Config(molecule_file=util.abs_path(c), args=args,
        command_args=command_args, ansible_args=ansible_args) for c in glob
        .glob(MOLECULE_GLOB)]
    _verify_configs(configs)
    return configs