def delete(self):
    if lib.EnvDeleteInstance(self._env, self._ist) != 1:
        raise CLIPSError(self._env)