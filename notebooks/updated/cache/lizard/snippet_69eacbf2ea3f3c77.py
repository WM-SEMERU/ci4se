def run_migrations_online(config):
    connectable = engine_from_config(config.get_section(config.
        config_ini_section), prefix='sqlalchemy.', poolclass=pool.NullPool)
    with connectable.connect() as connection:
        alembic.context.configure(connection=connection)
        with alembic.context.begin_transaction():
            alembic.context.run_migrations()