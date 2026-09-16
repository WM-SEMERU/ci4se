def execute(self):
    self._collect_garbage()
    upstream_channels = {}
    for node in nx.topological_sort(self.logical_topo):
        operator = self.operators[node]
        downstream_channels = self._generate_channels(operator)
        handles = self.__generate_actors(operator, upstream_channels,
            downstream_channels)
        if handles:
            self.actor_handles.extend(handles)
        upstream_channels.update(downstream_channels)
    logger.debug('Running...')
    return self.actor_handles