def _generate_scene_func(self, gen, func_name, create_new_scene, *args, **
    kwargs):
    new_gen = self._call_scene_func(gen, func_name, create_new_scene, *args,
        **kwargs)
    new_gen = new_gen if self.is_generator else list(new_gen)
    if create_new_scene:
        return self.__class__(new_gen)
    self._scene_gen = _SceneGenerator(new_gen)
    self._scenes = iter(self._scene_gen)