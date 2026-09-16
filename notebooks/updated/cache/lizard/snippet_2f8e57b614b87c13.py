def up(tag, sql, revision):
    alembic_command.upgrade(config=get_config(), revision=revision, sql=sql,
        tag=tag)