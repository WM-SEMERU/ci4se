def reset(self, indices=None):
    if indices is None:
        indices = np.arange(self.trajectories.batch_size)
    if indices.size == 0:
        tf.logging.warning(
            '`reset` called with empty indices array, this is a no-op.')
        return None
    observations = self._reset(indices)
    processed_observations = self.process_observations(observations)
    self.trajectories.reset(indices, observations)
    return processed_observations