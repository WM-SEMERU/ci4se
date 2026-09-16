def add_cluster(self, name, server=None, certificate_authority_data=None,
    **attrs):
    if self.cluster_exists(name):
        raise KubeConfError('Cluster with the given name already exists.')
    clusters = self.get_clusters()
    new_cluster = {'name': name, 'cluster': {}}
    attrs_ = new_cluster['cluster']
    if server is not None:
        attrs_['server'] = server
    if certificate_authority_data is not None:
        attrs_['certificate-authority-data'] = certificate_authority_data
    attrs_.update(attrs)
    clusters.append(new_cluster)