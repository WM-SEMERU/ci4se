def nearest_neighbor_threshold(self, vectors, threshold=0.5, batch_size=100,
    show_progressbar=False, return_names=True):
    vectors = np.array(vectors)
    if np.ndim(vectors) == 1:
        vectors = vectors[(None), :]
    result = []
    result = self._threshold_batch(vectors, batch_size, threshold,
        show_progressbar, return_names)
    return list(result)