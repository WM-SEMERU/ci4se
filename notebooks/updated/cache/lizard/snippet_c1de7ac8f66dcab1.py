def sampling_volume(self, val):
    if self.instrument == 'Vectrino' and type(val) is float:
        if val == 2.5:
            self.pdx.SamplingVolume = 0
        elif val == 4.0:
            self.pdx.SamplingVolume = 1
        elif val == 5.5:
            self.pdx.SamplingVolume = 2
        elif val == 7.0:
            self.pdx.SamplingVolume = 3
        elif val == 8.5:
            self.pdx.SamplingVolume = 4
        else:
            raise ValueError('Invalid sampling volume specified')
    elif val in range(5):
        self.pdx.SamplingVolume = val
    else:
        raise ValueError('Invalid sampling volume specified')