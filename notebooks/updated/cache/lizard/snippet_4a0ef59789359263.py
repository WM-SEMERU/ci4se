def enable_availability_zones(self, load_balancer_name, zones_to_add):
    params = {'LoadBalancerName': load_balancer_name}
    self.build_list_params(params, zones_to_add, 'AvailabilityZones.member.%d')
    return self.get_list('EnableAvailabilityZonesForLoadBalancer', params, None
        )