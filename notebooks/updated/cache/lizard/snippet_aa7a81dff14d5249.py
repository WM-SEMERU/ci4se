def configure_nodes(self):
    required_nodes = self._get_required_nodes()
    log.debug('Matching existing lb nodes to required %s (port %s)' % (', '
        .join(required_nodes), self.backend_port))
    self.consul.match_lb_nodes(self.lb_attrs[A.loadbalancer.ID], self.
        lb_attrs[A.loadbalancer.NODES_KEY], required_nodes, self.backend_port)
    self.lb_attrs = self.consul.lb_details(self.lb_attrs[A.loadbalancer.ID])