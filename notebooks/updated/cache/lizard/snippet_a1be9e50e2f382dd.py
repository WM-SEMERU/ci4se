def fit_freq_min_max(self, training_signal):
    window_length = len(self.window)
    window_weight = sum(self.window)
    max_mask = np.zeros(int(window_length / 2) + 1)
    min_mask = np.zeros(int(window_length / 2) + 1)
    for i in range(0, len(training_signal) - window_length - 1):
        rfft = np.fft.rfft(training_signal[i:i + window_length] * self.window)
        temp = np.abs(rfft) / window_weight
        max_mask = np.maximum(max_mask, temp)
        min_mask = np.minimum(min_mask, temp)
    self.mask_top = self.gain * max_mask
    self.mask_bottom = min_mask / self.gain