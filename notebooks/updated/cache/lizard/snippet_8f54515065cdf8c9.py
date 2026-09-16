def get_local_lb(self, loadbal_id, **kwargs):
    if 'mask' not in kwargs:
        kwargs['mask'] = (
            'loadBalancerHardware[datacenter], ipAddress, virtualServers[serviceGroups[routingMethod,routingType,services[healthChecks[type], groupReferences, ipAddress]]]'
            )
    return self.lb_svc.getObject(id=loadbal_id, **kwargs)