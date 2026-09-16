def run_migrations_offline():
    url = config.get_main_option('sqlalchemy.url')
    context.configure(url=url, target_metadata=target_metadata,
        literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()