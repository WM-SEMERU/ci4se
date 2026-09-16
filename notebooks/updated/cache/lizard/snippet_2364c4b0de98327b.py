def batch_indices_iterator(self, batch_size, shuffle=None, **kwargs):
    shuffle_rng = self._get_shuffle_rng(shuffle)
    if shuffle_rng is not None:
        return self.sampler.shuffled_indices_batch_iterator(batch_size,
            shuffle_rng)
    else:
        return self.sampler.in_order_indices_batch_iterator(batch_size)