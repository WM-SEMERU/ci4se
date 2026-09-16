def create_cluster(self, project_id, region, cluster, request_id=None,
    retry=google.api_core.gapic_v1.method.DEFAULT, timeout=google.api_core.
    gapic_v1.method.DEFAULT, metadata=None):
    if 'create_cluster' not in self._inner_api_calls:
        self._inner_api_calls['create_cluster'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            create_cluster, default_retry=self._method_configs[
            'CreateCluster'].retry, default_timeout=self._method_configs[
            'CreateCluster'].timeout, client_info=self._client_info)
    request = clusters_pb2.CreateClusterRequest(project_id=project_id,
        region=region, cluster=cluster, request_id=request_id)
    operation = self._inner_api_calls['create_cluster'](request, retry=
        retry, timeout=timeout, metadata=metadata)
    return google.api_core.operation.from_gapic(operation, self.transport.
        _operations_client, clusters_pb2.Cluster, metadata_type=
        proto_operations_pb2.ClusterOperationMetadata)