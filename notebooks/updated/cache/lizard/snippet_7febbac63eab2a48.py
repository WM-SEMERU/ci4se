def check_cluster_exists(self, name):
    self.kubeconf.open()
    clusters = self.kubeconf.get_clusters()
    names = [c['name'] for c in clusters]
    if name in names:
        return True
    return False