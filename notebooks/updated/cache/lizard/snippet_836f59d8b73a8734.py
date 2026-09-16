def to_human_readable(self, data, label_batch_entries=True, indices=None,
    sep='\n'):
    obs = data[0]
    batch_size = obs.shape[1]
    result = []
    indices = xrange(batch_size) if not indices else indices
    for b in indices:
        index_seq = np.argmax(obs[:, (b)], axis=1)
        prefix = 'b_{}: '.format(b) if label_batch_entries else ''
        result.append(prefix + self._data_source.decode(index_seq))
    return sep.join(result)