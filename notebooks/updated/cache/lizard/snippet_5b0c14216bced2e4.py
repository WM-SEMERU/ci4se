def get_all_addresses(self, addresses=None, filters=None, allocation_ids=None):
    params = {}
    if addresses:
        self.build_list_params(params, addresses, 'PublicIp')
    if allocation_ids:
        self.build_list_params(params, allocation_ids, 'AllocationId')
    if filters:
        self.build_filter_params(params, filters)
    return self.get_list('DescribeAddresses', params, [('item', Address)],
        verb='POST')