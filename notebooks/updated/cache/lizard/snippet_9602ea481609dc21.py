def get_meta_clusters(self, clusters):
    meta_clusters = collections.defaultdict(list)
    for cluster in clusters:
        if not cluster.meta_cluster:
            continue
        meta_clusters[cluster.meta_cluster].append(cluster)
    unconfigured_meta_clusters = [name for name in meta_clusters.keys() if 
        name not in self.meta_clusters]
    for name in unconfigured_meta_clusters:
        logger.error('Meta cluster %s not configured!')
        del meta_clusters[name]
    return meta_clusters