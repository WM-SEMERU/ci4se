def transform_audio(self, y):
    n_frames = self.n_frames(get_duration(y=y, sr=self.sr))
    D = stft(y, hop_length=self.hop_length, n_fft=self.n_fft)
    D = fix_length(D, n_frames)
    mag, phase = magphase(D)
    if self.log:
        mag = amplitude_to_db(mag, ref=np.max)
    return {'mag': mag.T[self.idx].astype(np.float32), 'phase': np.angle(
        phase.T)[self.idx].astype(np.float32)}