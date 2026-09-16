def cluster_exists(self, name):
    clusters = self.data['clusters']
    for cluster in clusters:
        if cluster['name'] == name:
            return True
    return False