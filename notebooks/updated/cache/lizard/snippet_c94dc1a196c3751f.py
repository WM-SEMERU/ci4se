def _update_centers(X, membs, n_clusters, distance):
    centers = np.empty(shape=(n_clusters, X.shape[1]), dtype=float)
    sse = np.empty(shape=n_clusters, dtype=float)
    for clust_id in range(n_clusters):
        memb_ids = np.where(membs == clust_id)[0]
        X_clust = X[(memb_ids), :]
        dist = np.empty(shape=memb_ids.shape[0], dtype=float)
        for i, x in enumerate(X_clust):
            dist[i] = np.sum(scipy.spatial.distance.cdist(X_clust, np.array
                ([x]), distance))
        inx_min = np.argmin(dist)
        centers[(clust_id), :] = X_clust[(inx_min), :]
        sse[clust_id] = dist[inx_min]
    return centers, sse