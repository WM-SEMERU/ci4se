def gmean(data, channels=None):
    if channels is None:
        data_stats = data
    else:
        data_stats = data[:, (channels)]
    return scipy.stats.gmean(data_stats, axis=0)