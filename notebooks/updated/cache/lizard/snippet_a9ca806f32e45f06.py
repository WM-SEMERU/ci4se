def current(directory=None, verbose=False, head_only=False):
    config = current_app.extensions['migrate'].migrate.get_config(directory)
    if alembic_version >= (0, 7, 0):
        command.current(config, verbose=verbose, head_only=head_only)
    else:
        command.current(config)