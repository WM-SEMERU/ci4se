def supportedGdalRasterFormats(cls, sqlAlchemyEngineOrSession):
    if isinstance(sqlAlchemyEngineOrSession, Engine):
        sessionMaker = sessionmaker(bind=sqlAlchemyEngineOrSession)
        session = sessionMaker()
    elif isinstance(sqlAlchemyEngineOrSession, Session):
        session = sqlAlchemyEngineOrSession
    statement = 'SELECT * FROM st_gdaldrivers() ORDER BY short_name;'
    result = session.execute(statement)
    supported = dict()
    for row in result:
        supported[row[1]] = {'description': row[2], 'options': row[3]}
    return supported