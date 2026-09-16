def fetch(self):
    if self.id == ApiCommand.SYNCHRONOUS_COMMAND_ID:
        return self
    resp = self._get_resource_root().get(self._path())
    return ApiCommand.from_json_dict(resp, self._get_resource_root())