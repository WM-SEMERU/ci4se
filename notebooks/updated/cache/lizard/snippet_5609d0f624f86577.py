def write_wav(self, filename):
    wave_output = None
    try:
        wave_output = wave.open(filename, 'w')
        wave_output.setparams(WAVE_PARAMS)
        frames = bytearray([(x << 4) for x in self.sample_data])
        wave_output.writeframes(frames)
    finally:
        if wave_output is not None:
            wave_output.close()