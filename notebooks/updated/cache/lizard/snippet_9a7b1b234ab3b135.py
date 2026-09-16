def get_all_reserved_instances(self, reserved_instances_id=None, filters=None):
    params = {}
    if reserved_instances_id:
        self.build_list_params(params, reserved_instances_id,
            'ReservedInstancesId')
    if filters:
        self.build_filter_params(params, filters)
    return self.get_list('DescribeReservedInstances', params, [('item',
        ReservedInstance)], verb='POST')