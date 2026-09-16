def set_samplerate(self, rate):
    float(rate)
    self.conconf.set_condition('samplerate', rate)
    if not self.no_auto:
        self.make_mask()