def __get_ra_index_indices(self):
    fragment_indices = []
    for idx, cumlen in enumerate(self._cumulative_lengths):
        cumlen_prev = self._cumulative_lengths[idx - 1] if idx > 0 else 0
        fragment_indices.append([np.argwhere(np.logical_and(self.ra_indices >=
            cumlen_prev, self.ra_indices < cumlen))])
    return fragment_indices