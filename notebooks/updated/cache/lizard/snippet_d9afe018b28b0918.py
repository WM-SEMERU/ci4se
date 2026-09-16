def create(self, networkipv6s):
    data = {'networks': networkipv6s}
    return super(ApiNetworkIPv6, self).post('api/v3/networkv6/', data)