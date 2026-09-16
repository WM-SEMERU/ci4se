def fit(self, sequences, y=None):
    self._initialized = False
    check_iter_of_sequences(sequences, max_iter=3)
    for X in sequences:
        self._fit(X)
    if self.n_sequences_ == 0:
        raise ValueError('All sequences were shorter than the lag time, %d' %
            self.lag_time)
    return self