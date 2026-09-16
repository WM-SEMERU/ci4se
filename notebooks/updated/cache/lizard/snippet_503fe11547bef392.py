def inverse(self, encoded, duration=None):
    ann = jams.Annotation(namespace=self.namespace, duration=duration)
    for start, end, value in self.decode_intervals(encoded, duration=
        duration, transition=self.transition, p_init=self.p_init, p_state=
        self.p_state):
        f_start, f_end = time_to_frames([start, end], sr=self.sr,
            hop_length=self.hop_length)
        confidence = np.mean(encoded[f_start:f_end + 1, (value)])
        value_dec = self.encoder.inverse_transform(np.atleast_2d(value))[0]
        for vd in value_dec:
            ann.append(time=start, duration=end - start, value=vd,
                confidence=confidence)
    return ann