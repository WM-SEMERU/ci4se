def by_id(cls, _id, engine_or_session):
    ses, auto_close = ensure_session(engine_or_session)
    obj = ses.query(cls).get(_id)
    if auto_close:
        ses.close()
    return obj