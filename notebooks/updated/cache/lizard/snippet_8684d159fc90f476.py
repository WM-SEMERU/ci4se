def reload(self):
    api = self._instance._client.database_admin_api
    metadata = _metadata_with_prefix(self.name)
    response = api.get_database_ddl(self.name, metadata=metadata)
    self._ddl_statements = tuple(response.statements)