def _group_adjacency(self, clusters, adj_list, counts):
    groups = []
    for cluster in clusters:
        if len(cluster) == 1:
            groups.append(list(cluster))
        else:
            observed = set()
            lead_umis = self._get_best_min_account(cluster, adj_list, counts)
            observed.update(lead_umis)
            for lead_umi in lead_umis:
                connected_nodes = set(adj_list[lead_umi])
                groups.append([lead_umi] + list(connected_nodes - observed))
                observed.update(connected_nodes)
    return groups