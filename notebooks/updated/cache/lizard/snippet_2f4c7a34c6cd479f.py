def _verify_same_spaces(self):
    if self._envs is None:
        raise ValueError('Environments not initialized.')
    if not isinstance(self._envs, list):
        tf.logging.warning(
            'Not checking observation and action space compatibility across envs, since there is just one.'
            )
        return
    if not all(str(env.observation_space) == str(self.observation_space) for
        env in self._envs):
        err_str = (
            "All environments should have the same observation space, but don't."
            )
        tf.logging.error(err_str)
        for i, env in enumerate(self._envs):
            tf.logging.error('Env[%d] has observation space [%s]', i, env.
                observation_space)
        raise ValueError(err_str)
    if not all(str(env.action_space) == str(self.action_space) for env in
        self._envs):
        err_str = (
            "All environments should have the same action space, but don't.")
        tf.logging.error(err_str)
        for i, env in enumerate(self._envs):
            tf.logging.error('Env[%d] has action space [%s]', i, env.
                action_space)
        raise ValueError(err_str)