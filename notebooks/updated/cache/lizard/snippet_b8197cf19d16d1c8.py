def configuration_from_uri(cls, persistence_uri):
    db_uri, persistence_state_id = cls.parse_persistence_uri(persistence_uri)
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    job = session.query(Job).filter(Job.id == persistence_state_id).first()
    configuration = job.configuration
    configuration = yaml.safe_load(configuration)
    configuration['exporter_options']['resume'] = True
    configuration['exporter_options']['persistence_state_id'
        ] = persistence_state_id
    return configuration