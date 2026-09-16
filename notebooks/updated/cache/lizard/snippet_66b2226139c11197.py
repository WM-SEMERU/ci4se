def get_rms(self):
    return np.sqrt(np.mean(np.square(self._entry_scores)))