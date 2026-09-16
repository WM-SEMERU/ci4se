def get_by_id(self, id_networkv6):
    uri = 'api/networkv4/%s/' % id_networkv6
    return super(ApiNetworkIPv6, self).get(uri)