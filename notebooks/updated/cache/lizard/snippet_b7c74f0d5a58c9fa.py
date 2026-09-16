def create_cluster(self, parent, cluster_id, cluster, retry=google.api_core
    .gapic_v1.method.DEFAULT, timeout=google.api_core.gapic_v1.method.
    DEFAULT, metadata=None):
    if 'create_cluster' not in self._inner_api_calls:
        self._inner_api_calls['create_cluster'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            create_cluster, default_retry=self._method_configs[
            'CreateCluster'].retry, default_timeout=self._method_configs[
            'CreateCluster'].timeout, client_info=self._client_info)
    request = bigtable_instance_admin_pb2.CreateClusterRequest(parent=
        parent, cluster_id=cluster_id, cluster=cluster)
    if metadata is None:
        metadata = []
    metadata = list(metadata)
    try:
        routing_header = [('parent', parent)]
    except AttributeError:
        pass
    else:
        routing_metadata = (google.api_core.gapic_v1.routing_header.
            to_grpc_metadata(routing_header))
        metadata.append(routing_metadata)
    operation = self._inner_api_calls['create_cluster'](request, retry=
        retry, timeout=timeout, metadata=metadata)
    return google.api_core.operation.from_gapic(operation, self.transport.
        _operations_client, instance_pb2.Cluster, metadata_type=
        bigtable_instance_admin_pb2.CreateClusterMetadata)