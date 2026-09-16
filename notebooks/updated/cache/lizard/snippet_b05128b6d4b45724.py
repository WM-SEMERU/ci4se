def statistical_distances(samples1, samples2, earth_mover_dist=True,
    energy_dist=True):
    out = []
    temp = scipy.stats.ks_2samp(samples1, samples2)
    out.append(temp.pvalue)
    out.append(temp.statistic)
    if earth_mover_dist:
        out.append(scipy.stats.wasserstein_distance(samples1, samples2))
    if energy_dist:
        out.append(scipy.stats.energy_distance(samples1, samples2))
    return np.asarray(out)