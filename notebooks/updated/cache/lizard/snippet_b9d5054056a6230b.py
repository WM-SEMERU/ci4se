def list_clusters(self):
    resp = self.instance_admin_client.list_clusters(self.
        instance_admin_client.instance_path(self.project, '-'))
    clusters = []
    instances = {}
    for cluster in resp.clusters:
        match_cluster_name = _CLUSTER_NAME_RE.match(cluster.name)
        instance_id = match_cluster_name.group('instance')
        if instance_id not in instances:
            instances[instance_id] = self.instance(instance_id)
        clusters.append(Cluster.from_pb(cluster, instances[instance_id]))
    return clusters, resp.failed_locations