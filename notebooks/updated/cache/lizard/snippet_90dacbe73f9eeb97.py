def butter_apply(b, a, data):
    import scipy.signal
    return scipy.signal.filtfilt(b, a, data, method='gust')