def delete_object(self, object_name):
    self._client.remove_object(self._instance, self.name, object_name)