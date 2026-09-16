def outliers_grubbs(x, hypo=False, alpha=0.05):
    val = np.max(np.abs(x - np.mean(x)))
    ind = np.argmax(np.abs(x - np.mean(x)))
    G = val / np.std(x, ddof=1)
    N = len(x)
    result = G > (N - 1) / np.sqrt(N) * np.sqrt(t.ppf(1 - alpha / (2 * N), 
        N - 2) ** 2 / (N - 2 + t.ppf(1 - alpha / (2 * N), N - 2) ** 2))
    if hypo:
        return result
    elif result:
        return np.delete(x, ind)
    else:
        return x