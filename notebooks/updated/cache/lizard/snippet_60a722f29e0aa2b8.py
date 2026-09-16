def run(self, cluster_config, rg_parser, partition_measurer,
    cluster_balancer, args):
    self.cluster_config = cluster_config
    self.args = args
    with ZK(self.cluster_config) as self.zk:
        self.log.debug('Starting %s for cluster: %s and zookeeper: %s',
            self.__class__.__name__, self.cluster_config.name, self.
            cluster_config.zookeeper)
        brokers = self.zk.get_brokers()
        assignment = self.zk.get_cluster_assignment()
        pm = partition_measurer(self.cluster_config, brokers, assignment, args)
        ct = ClusterTopology(assignment, brokers, pm, rg_parser.
            get_replication_group)
        if len(ct.partitions) == 0:
            self.log.info('The cluster is empty. No actions to perform.')
            return
        if self.is_reassignment_pending():
            self.log.error('Previous reassignment pending.')
            sys.exit(1)
        self.run_command(ct, cluster_balancer(ct, args))