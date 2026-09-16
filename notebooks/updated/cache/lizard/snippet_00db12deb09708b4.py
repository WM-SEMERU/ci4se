def remove_service(self, zconf, typ, name):
    _LOGGER.debug('remove_service %s, %s', typ, name)
    service = self.services.pop(name, None)
    if not service:
        _LOGGER.debug('remove_service unknown %s, %s', typ, name)
        return
    if self.remove_callback:
        self.remove_callback(name, service)