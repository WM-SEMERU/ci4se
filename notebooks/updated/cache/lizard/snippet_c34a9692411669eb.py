def setConnection(self, connection):
    if not isinstance(connection, orb.Connection):
        conn = orb.Connection.byName(connection)
        if not conn:
            raise orb.errors.BackendNotFound(connection)
        connection = conn(self)
    else:
        connection.setDatabase(self)
    self.__connection = connection