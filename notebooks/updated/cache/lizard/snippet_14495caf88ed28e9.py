def template(self):
    return Template(self._env, lib.EnvFactDeftemplate(self._env, self._fact))