def make_alembic_config(temporary_dir, migrations_dir):
    config = Config()
    config.set_main_option('temporary_dir', temporary_dir)
    config.set_main_option('migrations_dir', migrations_dir)
    return config