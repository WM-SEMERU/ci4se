def median(data, channels=None):
    if channels is None:
        data_stats = data
    else:
        data_stats = data[:, (channels)]
    return np.median(data_stats, axis=0)