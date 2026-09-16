def filter(self, zone='all'):
    if not self.is_connected():
        return None
    nodes = self.gce.list_nodes(zone)
    return Filter(nodes)