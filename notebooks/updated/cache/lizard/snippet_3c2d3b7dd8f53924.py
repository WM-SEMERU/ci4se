def get_associated_uplink_groups(self):
    uri = '{}/associatedUplinkGroups'.format(self.data['uri'])
    return self._helper.do_get(uri)