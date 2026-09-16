async def refresh(self):
    raw_data = await self.request.get(self._resource_path, {'refresh': 'true'})
    self._raw_data = raw_data[ATTR_SHADE]