def _build_instance_group_args(self, instance_group):
    params = {'InstanceCount': instance_group.num_instances, 'InstanceRole':
        instance_group.role, 'InstanceType': instance_group.type, 'Name':
        instance_group.name, 'Market': instance_group.market}
    if instance_group.market == 'SPOT':
        params['BidPrice'] = instance_group.bidprice
    return params