def adaptive_knn_graph(traj_dist, k):
    adj_mat = np.zeros_like(traj_dist, dtype=float)
    knn = np.transpose(np.argsort(traj_dist, 0))
    for i in range(0, traj_dist.shape[0]):
        adj_mat[i, knn[i, range(1, k)]] = traj_dist[i, knn[i, range(1, k)]]
    return adj_mat