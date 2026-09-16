def start(self, min_nodes=None):
    nodes = self.get_all_nodes()
    log.info('Starting cluster nodes ...')
    if log.DO_NOT_FORK:
        nodes = self._start_nodes_sequentially(nodes)
    else:
        nodes = self._start_nodes_parallel(nodes, self.thread_pool_max_size)
    self.repository.save_or_update(self)
    not_started_nodes = self._check_starting_nodes(nodes, self.startup_timeout)
    self.repository.save_or_update(self)
    log.info('Checking SSH connection to nodes ...')
    pending_nodes = nodes - not_started_nodes
    self._gather_node_ip_addresses(pending_nodes, self.startup_timeout)
    self.repository.save_or_update(self)
    min_nodes = self._compute_min_nodes(min_nodes)
    self._check_cluster_size(min_nodes)