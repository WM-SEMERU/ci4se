async def deserialize(self, data: dict, silent=True):
    self.import_data(self._deserialize(data))
    self.validate()