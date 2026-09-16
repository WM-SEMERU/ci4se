def database_to_intermediary(database_uri, schema=None):
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy import create_engine
    Base = automap_base()
    engine = create_engine(database_uri)
    if schema is not None:
        Base.metadata.schema = schema
    Base.prepare(engine, reflect=True, name_for_scalar_relationship=
        name_for_scalar_relationship)
    return declarative_to_intermediary(Base)