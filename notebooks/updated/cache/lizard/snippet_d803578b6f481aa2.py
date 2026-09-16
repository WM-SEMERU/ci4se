def make_butterworth_bandpass_b_a(CenterFreq, bandwidth, SampleFreq, order=
    5, btype='band'):
    lowcut = CenterFreq - bandwidth / 2
    highcut = CenterFreq + bandwidth / 2
    b, a = make_butterworth_b_a(lowcut, highcut, SampleFreq, order, btype)
    return b, a