def _step(self, actions):
    self.assert_common_preconditions()
    assert len(actions) == len(self._envs)
    observations = []
    rewards = []
    dones = []
    infos = []
    for env, action in zip(self._envs, actions):
        observation, reward, done, info = env.step(action)
        observations.append(observation)
        rewards.append(reward)
        dones.append(done)
        infos.append(info)
    return tuple(map(np.stack, [observations, rewards, dones, infos]))