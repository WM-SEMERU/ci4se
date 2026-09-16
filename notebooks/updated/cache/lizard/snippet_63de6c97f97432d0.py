def new_instance(self, name):
    ist = lib.EnvCreateRawInstance(self._env, self._cls, name.encode())
    if ist == ffi.NULL:
        raise CLIPSError(self._env)
    return Instance(self._env, ist)