def _get_reserved_instance_count(self):
    reservations = defaultdict(int)
    az_to_res = {}
    logger.debug('Getting reserved instance information')
    res = self.conn.describe_reserved_instances()
    for x in res['ReservedInstances']:
        if x['State'] != 'active':
            logger.debug('Skipping ReservedInstance %s with state %s', x[
                'ReservedInstancesId'], x['State'])
            continue
        if 'AvailabilityZone' not in x:
            x['AvailabilityZone'] = RI_NO_AZ
        if x['AvailabilityZone'] not in az_to_res:
            az_to_res[x['AvailabilityZone']] = deepcopy(reservations)
        az_to_res[x['AvailabilityZone']][x['InstanceType']] += x[
            'InstanceCount']
    for x in az_to_res:
        az_to_res[x] = dict(az_to_res[x])
    return az_to_res