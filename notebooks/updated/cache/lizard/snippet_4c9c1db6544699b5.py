def rollout(self, **kwargs):
    if kwargs.has_key('tau'):
        timesteps = int(self.timesteps / kwargs['tau'])
    else:
        timesteps = self.timesteps
    self.x_track = np.zeros(timesteps)
    self.reset_state()
    for t in range(timesteps):
        self.x_track[t] = self.x
        self.step(**kwargs)
    return self.x_track