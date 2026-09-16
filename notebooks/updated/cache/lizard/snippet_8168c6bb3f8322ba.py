def validate_resource_uri(self, path):
    if self._base_uri not in path:
        logger.exception('Get by uri : unrecognized uri: (%s)' % path)
        raise exceptions.HPOneViewUnknownType(UNRECOGNIZED_URI)