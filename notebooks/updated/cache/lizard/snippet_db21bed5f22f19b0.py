def run_migrations_online():

    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info('No changes in schema detected.')
    engine = engine_from_config(config.get_section(config.
        config_ini_section), prefix='sqlalchemy.', poolclass=pool.NullPool)
    connection = engine.connect()
    kwargs = {}
    if engine.name in ('sqlite', 'mysql'):
        kwargs = {'transaction_per_migration': True, 'transactional_ddl': True}
    configure_args = current_app.extensions['migrate'].configure_args
    if configure_args:
        kwargs.update(configure_args)
    context.configure(connection=connection, target_metadata=
        target_metadata, process_revision_directives=
        process_revision_directives, **kwargs)
    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()