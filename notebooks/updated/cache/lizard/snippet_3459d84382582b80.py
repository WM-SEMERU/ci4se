def name(self):
    return ffi.string(lib.EnvGetDefglobalName(self._env, self._glb)).decode()