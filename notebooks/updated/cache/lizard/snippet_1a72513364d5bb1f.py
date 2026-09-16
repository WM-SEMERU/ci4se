def add_service_group(self, lb_id, allocation=100, port=80, routing_type=2,
    routing_method=10):
    mask = 'virtualServers[serviceGroups[services[groupReferences]]]'
    load_balancer = self.lb_svc.getObject(id=lb_id, mask=mask)
    service_template = {'port': port, 'allocation': allocation,
        'serviceGroups': [{'routingTypeId': routing_type, 'routingMethodId':
        routing_method}]}
    load_balancer['virtualServers'].append(service_template)
    return self.lb_svc.editObject(load_balancer, id=lb_id)