def _frame_generator(self, frame_duration_ms, audio, sample_rate):
    n = int(sample_rate * (frame_duration_ms / 1000.0) * 2)
    offset = 0
    timestamp = 0.0
    duration = float(n) / sample_rate / 2.0
    while offset + n < len(audio):
        yield self.Frame(audio[offset:offset + n], timestamp, duration)
        timestamp += duration
        offset += n