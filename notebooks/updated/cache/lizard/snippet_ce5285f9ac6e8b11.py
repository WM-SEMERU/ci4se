def get_cluster_name(self):
    return self._get(url=self.url + '/api/cluster-name', headers=self.
        headers, auth=self.auth)