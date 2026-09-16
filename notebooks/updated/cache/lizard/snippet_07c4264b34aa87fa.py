def ppf(q, df, loc=0.0, scale=1.0, gamma=1.0):
    result = np.zeros(q.shape[0])
    probzero = Skewt.cdf(x=np.zeros(1), loc=np.zeros(1), df=df, gamma=gamma)
    result[q < probzero] = 1.0 / gamma * ss.t.ppf((np.power(gamma, 2) + 1.0
        ) * q[q < probzero] / 2.0, df)
    result[q >= probzero] = gamma * ss.t.ppf((1.0 + 1.0 / np.power(gamma, 2
        )) / 2.0 * (q[q >= probzero] - probzero) + 0.5, df)
    return result