def filterbanks(num_filter, coefficients, sampling_freq, low_freq=None,
    high_freq=None):
    high_freq = high_freq or sampling_freq / 2
    low_freq = low_freq or 300
    s = 'High frequency cannot be greater than half of the sampling frequency!'
    assert high_freq <= sampling_freq / 2, s
    assert low_freq >= 0, 'low frequency cannot be less than zero!'
    mels = np.linspace(functions.frequency_to_mel(low_freq), functions.
        frequency_to_mel(high_freq), num_filter + 2)
    hertz = functions.mel_to_frequency(mels)
    freq_index = np.floor((coefficients + 1) * hertz / sampling_freq).astype(
        int)
    filterbank = np.zeros([num_filter, coefficients])
    for i in range(0, num_filter):
        left = int(freq_index[i])
        middle = int(freq_index[i + 1])
        right = int(freq_index[i + 2])
        z = np.linspace(left, right, num=right - left + 1)
        filterbank[(i), left:right + 1] = functions.triangle(z, left=left,
            middle=middle, right=right)
    return filterbank