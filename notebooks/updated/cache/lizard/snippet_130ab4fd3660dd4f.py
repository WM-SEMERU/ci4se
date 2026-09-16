def parse_yaml_config(args):
    try:
        import yaml
    except ImportError:
        yaml = None
    yml = {}
    try:
        with open(args.coveralls_yaml, 'r') as fp:
            if not yaml:
                raise SystemExit('PyYAML is required for parsing configuration'
                    )
            yml = yaml.load(fp)
    except IOError:
        pass
    yml = yml or {}
    return yml