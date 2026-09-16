def _get_best_percentile(self, cluster, counts):
    if len(cluster) == 1:
        return list(cluster)
    else:
        threshold = np.median(list(counts.values())) / 100
        return [read for read in cluster if counts[read] > threshold]