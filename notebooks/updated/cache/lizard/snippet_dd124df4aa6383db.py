def _container_registration(self, alias):
    containers = Container.find_by_name(self._client_session, alias)

    def validate_name(name):
        valid = True
        if name in containers:
            valid = False
        return valid
    count = 1
    container_name = '{0}-0{1}'.format(alias, count)
    while not validate_name(container_name):
        count += 1
        container_index = count if count > 10 else '0{0}'.format(count)
        container_name = '{0}-{1}'.format(alias, container_index)
    return container_name