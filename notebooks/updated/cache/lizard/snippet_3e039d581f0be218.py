def _get_updated_environment(self, env_dict=None):
    if env_dict is None:
        env_dict = {'S': self}
    env = globals().copy()
    env.update(env_dict)
    return env