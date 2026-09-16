def get_pip_options(args=[], sources=None, pip_command=None):
    if not pip_command:
        pip_command = get_pip_command()
    if not sources:
        sources = [{'url': 'https://pypi.org/simple', 'name': 'pypi',
            'verify_ssl': True}]
    _ensure_dir(CACHE_DIR)
    pip_args = args
    pip_args = prepare_pip_source_args(sources, pip_args)
    pip_options, _ = pip_command.parser.parse_args(pip_args)
    pip_options.cache_dir = CACHE_DIR
    return pip_options