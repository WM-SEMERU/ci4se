def check_migrations_applied(migrate):
    errors = []
    from alembic.migration import MigrationContext
    from alembic.script import ScriptDirectory
    from sqlalchemy.exc import DBAPIError, SQLAlchemyError
    config = migrate.get_config(directory=migrate.directory)
    script = ScriptDirectory.from_config(config)
    try:
        with migrate.db.engine.connect() as connection:
            context = MigrationContext.configure(connection)
            db_heads = set(context.get_current_heads())
            script_heads = set(script.get_heads())
    except (DBAPIError, SQLAlchemyError) as e:
        msg = "Can't connect to database to check migrations: {!s}".format(e)
        return [Info(msg, id=health.INFO_CANT_CHECK_MIGRATIONS)]
    if db_heads != script_heads:
        msg = 'Unapplied migrations found: {}'.format(', '.join(script_heads))
        errors.append(Warning(msg, id=health.WARNING_UNAPPLIED_MIGRATION))
    return errors