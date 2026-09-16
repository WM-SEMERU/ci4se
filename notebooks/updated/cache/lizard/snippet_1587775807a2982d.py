def file_envs(self, load=None):
    if load is None:
        load = {}
    load.pop('cmd', None)
    return self.envs(**load)