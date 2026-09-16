def container_running(self, container_name):
    filters = {'name': container_name, 'status': 'running'}
    for container in self.client.containers.list(filters=filters):
        if container_name == container.name:
            return container
    return None