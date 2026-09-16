def get_trajectories(self, indexes, rollout_length):
    assert rollout_length > 1, 'Rollout length must be greater than 1'
    batch_indexes = indexes.reshape(1, indexes.shape[0]) - np.arange(
        rollout_length - 1, -1, -1).reshape(rollout_length, 1)
    return self.get_transitions(batch_indexes)