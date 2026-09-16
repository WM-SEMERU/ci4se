def calcstats(data, t1, t2, sr):
    dataseg = data[sr * t1:sr * t2]
    meandata = np.mean(dataseg[~np.isnan(dataseg)])
    stddata = np.std(dataseg[~np.isnan(dataseg)])
    return meandata, stddata