def do_clustering(types, max_clust):
    ls = [list(t[t.find('b') + 1:]) for t in types]
    prepend_zeros_to_lists(ls)
    dist_matrix = pdist(ls, weighted_hamming)
    clusters = hierarchicalcluster.complete(dist_matrix)
    clusters = hierarchicalcluster.fcluster(clusters, max_clust, criterion=
        'maxclust')
    cluster_dict = dict((c, []) for c in set(clusters))
    for i in range(len(types)):
        cluster_dict[clusters[i]].append(types[i])
    return cluster_dict