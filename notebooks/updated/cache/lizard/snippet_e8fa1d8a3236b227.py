def start(self, min_nodes=None, max_concurrent_requests=0):
    nodes = self.get_all_nodes()
    log.info('Starting cluster nodes (timeout: %d seconds) ...', self.
        start_timeout)
    if max_concurrent_requests == 0:
        try:
            max_concurrent_requests = 4 * get_num_processors()
        except RuntimeError:
            log.warning(
                'Cannot determine number of processors! will start nodes sequentially...'
                )
            max_concurrent_requests = 1
    if max_concurrent_requests > 1:
        nodes = self._start_nodes_parallel(nodes, max_concurrent_requests)
    else:
        nodes = self._start_nodes_sequentially(nodes)
    self.repository.save_or_update(self)
    not_started_nodes = self._check_starting_nodes(nodes, self.start_timeout)
    self.repository.save_or_update(self)
    started_nodes = nodes - not_started_nodes
    if not started_nodes:
        raise ClusterSizeError('No nodes could be started!')
    log.info('Checking SSH connection to nodes (timeout: %d seconds) ...',
        self.start_timeout)
    self._gather_node_ip_addresses(started_nodes, self.start_timeout, self.
        ssh_probe_timeout)
    self.repository.save_or_update(self)
    self._check_cluster_size(self._compute_min_nodes(min_nodes))