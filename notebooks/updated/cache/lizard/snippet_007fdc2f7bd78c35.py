def refresh(self):
    connection = self.model._meta.dj_connection
    return connection.connection.indices.refresh(indices=connection.database)