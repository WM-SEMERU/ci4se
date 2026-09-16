def connect_or_create(self, overwrite=False):
    connection = self._get_connection()
    if connection:
        return connection
    else:
        return self.create(overwrite=overwrite)