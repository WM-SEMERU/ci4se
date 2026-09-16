def types(self):
    data = clips.data.DataObject(self._env)
    lib.EnvSlotTypes(self._env, self._cls, self._name, data.byref)
    return tuple(data.value) if isinstance(data.value, list) else ()