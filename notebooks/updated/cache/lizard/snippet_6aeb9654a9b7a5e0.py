def get_network(self, org, segid):
    network_info = {'organizationName': org, 'partitionName': self.
        _part_name, 'segmentId': segid}
    res = self._get_network(network_info)
    if res and res.status_code in self._resp_ok:
        return res.json()