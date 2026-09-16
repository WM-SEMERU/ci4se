def delete(self):
    api = self._client.instance_admin_api
    metadata = _metadata_with_prefix(self.name)
    api.delete_instance(self.name, metadata=metadata)