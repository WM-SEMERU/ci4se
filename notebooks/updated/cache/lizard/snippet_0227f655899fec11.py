def amplitude_by_welch(self, data_frame):
    frq, Pxx_den = signal.welch(data_frame.filtered_signal.values, self.
        sampling_frequency, nperseg=self.window)
    freq = frq[Pxx_den.argmax(axis=0)]
    ampl = sum(Pxx_den[(frq > self.lower_frequency) & (frq < self.
        upper_frequency)])
    logging.debug('tremor amplitude by welch calculated')
    return ampl, freq