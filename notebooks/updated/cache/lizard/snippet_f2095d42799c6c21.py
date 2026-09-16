def IIR_filter_design(CentralFreq, bandwidth, transitionWidth, SampleFreq,
    GainStop=40, GainPass=0.01):
    NyquistFreq = SampleFreq / 2
    if CentralFreq + bandwidth / 2 + transitionWidth > NyquistFreq:
        raise ValueError(
            'Need a higher Sample Frequency for this Central Freq, Bandwidth and transition Width'
            )
    CentralFreqNormed = CentralFreq / NyquistFreq
    bandwidthNormed = bandwidth / NyquistFreq
    transitionWidthNormed = transitionWidth / NyquistFreq
    bandpass = [CentralFreqNormed - bandwidthNormed / 2, CentralFreqNormed +
        bandwidthNormed / 2]
    bandstop = [CentralFreqNormed - bandwidthNormed / 2 -
        transitionWidthNormed, CentralFreqNormed + bandwidthNormed / 2 +
        transitionWidthNormed]
    print(bandpass, bandstop)
    b, a = scipy.signal.iirdesign(bandpass, bandstop, GainPass, GainStop)
    return b, a