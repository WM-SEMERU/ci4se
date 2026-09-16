def sample(self, batch_size, batch_idxs=None):
    if batch_idxs is None:
        batch_idxs = sample_batch_indexes(0, self.nb_entries, size=batch_size)
    assert len(batch_idxs) == batch_size
    batch_params = []
    batch_total_rewards = []
    for idx in batch_idxs:
        batch_params.append(self.params[idx])
        batch_total_rewards.append(self.total_rewards[idx])
    return batch_params, batch_total_rewards