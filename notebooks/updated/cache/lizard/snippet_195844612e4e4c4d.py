def get_all_instances(self, instance_ids=None, filters=None):
    params = {}
    if instance_ids:
        self.build_list_params(params, instance_ids, 'InstanceId')
    if filters:
        if 'group-id' in filters:
            gid = filters.get('group-id')
            if not gid.startswith('sg-') or len(gid) != 11:
                warnings.warn(
                    "The group-id filter now requires a security group identifier (sg-*) instead of a group name. To filter by group name use the 'group-name' filter instead."
                    , UserWarning)
        self.build_filter_params(params, filters)
    return self.get_list('DescribeInstances', params, [('item', Reservation
        )], verb='POST')