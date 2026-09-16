def load_cli_config(args):
    default_cli_config = _load_default_cli_config()
    toml_config = _load_toml_cli_config()
    for config in (toml_config, default_cli_config):
        for key, val in config.items():
            if key in args and getattr(args, key) is not None:
                pass
            else:
                setattr(args, key, val)