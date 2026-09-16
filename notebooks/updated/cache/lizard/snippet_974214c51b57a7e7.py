def calcLogSum(Vals, sigma):
    if sigma == 0.0:
        V = np.amax(Vals, axis=0)
        return V
    maxV = np.max(Vals, axis=0)
    sumexp = np.sum(np.exp((Vals - maxV) / sigma), axis=0)
    LogSumV = np.log(sumexp)
    LogSumV = maxV + sigma * LogSumV
    return LogSumV