def get_all_internet_gateways(self, internet_gateway_ids=None, filters=None):
    params = {}
    if internet_gateway_ids:
        self.build_list_params(params, internet_gateway_ids,
            'InternetGatewayId')
    if filters:
        self.build_filter_params(params, dict(filters))
    return self.get_list('DescribeInternetGateways', params, [('item',
        InternetGateway)])