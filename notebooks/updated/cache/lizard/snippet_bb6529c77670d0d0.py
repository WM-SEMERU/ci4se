def clean(config=None, path=None, saltenv='base'):
    config_tree = tree(config=config, path=path, saltenv=saltenv)
    return _print_config_text(config_tree)