def list_clusters(self, project_id, zone, parent=None, retry=google.
    api_core.gapic_v1.method.DEFAULT, timeout=google.api_core.gapic_v1.
    method.DEFAULT, metadata=None):
    if 'list_clusters' not in self._inner_api_calls:
        self._inner_api_calls['list_clusters'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            list_clusters, default_retry=self._method_configs[
            'ListClusters'].retry, default_timeout=self._method_configs[
            'ListClusters'].timeout, client_info=self._client_info)
    request = cluster_service_pb2.ListClustersRequest(project_id=project_id,
        zone=zone, parent=parent)
    return self._inner_api_calls['list_clusters'](request, retry=retry,
        timeout=timeout, metadata=metadata)