def recall_service(self, service):
    if not isinstance(service, Service):
        raise TypeError('service must be of type Service.')
    logger.warning(
        'The deployment for {0} on {1} failed starting the rollback.'.
        format(service.alias, self.url.geturl()))

    def anonymous(anonymous_service):
        if not isinstance(anonymous_service, Service):
            raise TypeError('service must be an instance of Service.')
        containers = self.find_previous_service_containers(anonymous_service)
        if containers:
            for name in list(anonymous_service.containers.keys()):
                del anonymous_service.containers[name]
            anonymous_service.cargo.delete()
            for name, container in six.iteritems(containers):
                if container.state().get('running'):
                    logger.info(
                        'is already running... Might want to investigate.',
                        extra={'formatter': 'container', 'container':
                        container.name})
                elif container.start():
                    logger.info('is restarted and healthy.', extra={
                        'formatter': 'container', 'container': container.name})
                else:
                    logger.error('failed to start.', extra={'formatter':
                        'container', 'container': container.name})
                    container.dump_logs()
                    raise Exception(
                        'The deployment for {0} on {1} went horribly wrong'
                        .format(container.name, self.url.geturl()))
    self._service_map(service, anonymous, descending=False)