def get_pulse_s(self):
    try:
        dwelltime = self.ppg.dwelltime.mean
        beam_on = self.ppg.beam_on.mean
    except AttributeError:
        raise AttributeError('Missing logged ppg parameter: dwelltime ' +
            'or beam_on')
    return dwelltime * beam_on / 1000.0