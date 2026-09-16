async def delete_scene(self, scene_id: int):
    _scene = await self.get_scene(scene_id, from_cache=False)
    return await _scene.delete()