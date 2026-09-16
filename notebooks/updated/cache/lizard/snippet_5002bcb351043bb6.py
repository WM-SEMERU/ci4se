def exists(self):
    session = client.get_client().create_session()
    ret = self._base_query(session).count() > 0
    session.close()
    return ret