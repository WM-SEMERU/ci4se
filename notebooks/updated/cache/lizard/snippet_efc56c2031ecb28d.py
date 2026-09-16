def default_value(self):
    data = clips.data.DataObject(self._env)
    lib.EnvSlotDefaultValue(self._env, self._cls, self._name, data.byref)
    return data.value