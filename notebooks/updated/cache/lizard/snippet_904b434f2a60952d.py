def synthesize(self, duration):
    sr = self.samplerate.samples_per_second
    seconds = duration / Seconds(1)
    samples = np.random.uniform(low=-1.0, high=1.0, size=int(sr * seconds))
    return AudioSamples(samples, self.samplerate)