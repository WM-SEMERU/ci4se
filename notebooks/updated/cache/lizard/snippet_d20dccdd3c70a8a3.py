def transform_audio(self, y):
    n_frames = self.n_frames(get_duration(y=y, sr=self.sr))
    C = cqt(y=y, sr=self.sr, hop_length=self.hop_length, fmin=self.fmin,
        n_bins=self.n_octaves * self.over_sample * 12, bins_per_octave=self
        .over_sample * 12)
    C = fix_length(C, n_frames)
    cqtm, phase = magphase(C)
    if self.log:
        cqtm = amplitude_to_db(cqtm, ref=np.max)
    return {'mag': cqtm.T.astype(np.float32)[self.idx], 'phase': np.angle(
        phase).T.astype(np.float32)[self.idx]}