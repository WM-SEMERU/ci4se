def cardinality(self):
    data = clips.data.DataObject(self._env)
    lib.EnvDeftemplateSlotCardinality(self._env, self._tpl, self._name,
        data.byref)
    return tuple(data.value) if isinstance(data.value, list) else ()