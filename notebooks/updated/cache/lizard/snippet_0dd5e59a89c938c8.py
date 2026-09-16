def get_location_id(self, location):
    if isinstance(location, int):
        return location
    mask = 'mask[id,name,regions[keyname]]'
    if match('[a-zA-Z]{3}[0-9]{2}', location) is not None:
        search = {'name': {'operation': location}}
    else:
        search = {'regions': {'keyname': {'operation': location}}}
    datacenter = self.client.call('SoftLayer_Location', 'getDatacenters',
        mask=mask, filter=search)
    if len(datacenter) != 1:
        raise exceptions.SoftLayerError('Unable to find location: %s' %
            location)
    return datacenter[0]['id']