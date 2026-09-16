def delete(self):
    body = client.V1DeleteOptions()
    try:
        status = self.core_api.delete_namespaced_pod(self.name, self.
            namespace, body)
        logger.info('Deleting Pod %s in namespace %s', self.name, self.
            namespace)
        self.phase = PodPhase.TERMINATING
    except ApiException as e:
        raise ConuException(
            'Exception when calling Kubernetes API - delete_namespaced_pod: %s\n'
             % e)
    if status.status == 'Failure':
        raise ConuException('Deletion of Pod failed')