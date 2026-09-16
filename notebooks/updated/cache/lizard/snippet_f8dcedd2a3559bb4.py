def get_client(self, region):
    ep = self._ep_for_region(region)
    if not ep:
        raise exc.NoEndpointForRegion(
            "There is no endpoint defined for the region '%s' for the '%s' service."
             % (region, self.service_type))
    return ep.client