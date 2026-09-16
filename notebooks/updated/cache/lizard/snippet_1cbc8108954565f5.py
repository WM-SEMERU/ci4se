def _reset(self, indices):
    self.assert_common_preconditions()
    return np.stack([self._envs[index].reset() for index in indices])