def get_physical_port(self):
    obj = None
    if self.is_link_aggregation():
        obj = UnityLinkAggregation.get(self._cli, self.get_id())
    else:
        obj = UnityEthernetPort.get(self._cli, self.get_id())
    return obj