def gcv(data, channels=None):
    if channels is None:
        data_stats = data
    else:
        data_stats = data[:, (channels)]
    return np.sqrt(np.exp(np.std(np.log(data_stats), axis=0) ** 2) - 1)