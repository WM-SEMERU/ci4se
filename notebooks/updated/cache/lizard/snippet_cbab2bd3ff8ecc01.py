def _group_unique(self, clusters, adj_list, counts):
    if len(clusters) == 1:
        groups = [clusters]
    else:
        groups = [[x] for x in clusters]
    return groups