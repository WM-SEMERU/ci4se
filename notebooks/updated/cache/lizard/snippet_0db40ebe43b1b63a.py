def zero_crossing_after(self, n):
    n_in_samples = int(n * self.samplerate)
    search_end = n_in_samples + self.samplerate
    if search_end > self.duration:
        search_end = self.duration
    frame = zero_crossing_first(self.range_as_mono(n_in_samples, search_end)
        ) + n_in_samples
    return frame / float(self.samplerate)