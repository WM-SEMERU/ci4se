def ecg_find_peaks(signal, sampling_rate=1000):
    rpeaks, = biosppy.ecg.hamilton_segmenter(np.array(signal),
        sampling_rate=sampling_rate)
    rpeaks, = biosppy.ecg.correct_rpeaks(signal=np.array(signal), rpeaks=
        rpeaks, sampling_rate=sampling_rate, tol=0.05)
    return rpeaks