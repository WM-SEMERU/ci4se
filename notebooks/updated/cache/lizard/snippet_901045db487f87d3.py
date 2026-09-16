def transaction(self, session=None):
    local_session = None
    if session is None:
        local_session = session = self.create_scoped_session()
    try:
        yield session
    finally:
        if local_session is not None:
            pass