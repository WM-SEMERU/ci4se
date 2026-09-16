async def activate(self):
    _val = await self.request.get(self._base_path, params={ATTR_SCENE_ID:
        self._id})
    return _val