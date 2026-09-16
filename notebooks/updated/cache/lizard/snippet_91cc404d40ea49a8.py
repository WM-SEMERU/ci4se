def delete(self, cluster):
    if cluster.name not in self.clusters:
        raise ClusterNotFound('Unable to delete non-existent cluster %s' %
            cluster.name)
    del self.clusters[cluster.name]