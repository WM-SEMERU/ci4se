def name(self):
    return ffi.string(lib.EnvGetDefclassName(self._env, self._cls)).decode()