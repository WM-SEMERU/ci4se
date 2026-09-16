def __execute_text(self, query, **replacements):
    session = self.__get_session()
    try:
        records = session.execute(query, replacements)
    except:
        _LOGGER.exception('Query failure:\n%s', query)
        raise
    try:
        records = list(records)
    finally:
        session.commit()
    for record in records:
        yield dict(record)