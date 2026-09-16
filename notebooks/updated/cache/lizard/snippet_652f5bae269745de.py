def createdb():
    manager.db.engine.echo = True
    manager.db.create_all()
    set_alembic_revision()