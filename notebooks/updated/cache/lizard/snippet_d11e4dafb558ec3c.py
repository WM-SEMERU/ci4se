def watch(self, flag):
    lib.EnvSetDeftemplateWatch(self._env, int(flag), self._tpl)