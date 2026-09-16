def _run_algorithm(self):
    nan_entries = np.isnan(self._X)
    NNlist = [self._find_neighbors(datalen) for datalen in range(self._datalen)
        ]
    scores = np.sum(Parallel(n_jobs=self.n_jobs)(delayed(
        MultiSURF_compute_scores)(instance_num, self.attr, nan_entries,
        self._num_attributes, self.mcmap, NN_near, self._headers, self.
        _class_type, self._X, self._y, self._labels_std, self.data_type) for
        instance_num, NN_near in zip(range(self._datalen), NNlist)), axis=0)
    return np.array(scores)