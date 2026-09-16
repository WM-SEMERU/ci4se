def drop(self):
    api = self._instance._client.database_admin_api
    metadata = _metadata_with_prefix(self.name)
    api.drop_database(self.name, metadata=metadata)