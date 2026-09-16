def _conversion(self, input_signal, vad_file):
    e = bob.ap.Energy(rate_wavsample[0], self.win_length_ms, self.win_shift_ms)
    energy_array = e(rate_wavsample[1])
    labels = self.use_existing_vad(energy_array, vad_file)
    return labels