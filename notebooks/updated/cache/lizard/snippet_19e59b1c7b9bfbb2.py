def ecg_simulate(duration=10, sampling_rate=1000, bpm=60, noise=0.01):
    cardiac = scipy.signal.wavelets.daub(10)
    cardiac = np.concatenate([cardiac, np.zeros(10)])
    num_heart_beats = int(duration * bpm / 60)
    ecg = np.tile(cardiac, num_heart_beats)
    noise = np.random.normal(0, noise, len(ecg))
    ecg = noise + ecg
    ecg = scipy.signal.resample(ecg, sampling_rate * duration)
    return ecg