def instances(self):
    ist = lib.EnvGetNextInstanceInClass(self._env, self._cls, ffi.NULL)
    while ist != ffi.NULL:
        yield Instance(self._env, ist)
        ist = lib.EnvGetNextInstanceInClass(self._env, self._cls, ist)