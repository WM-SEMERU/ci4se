def express_route_cross_connection_peerings(self):
    api_version = self._get_api_version(
        'express_route_cross_connection_peerings')
    if api_version == '2018-02-01':
        from .v2018_02_01.operations import ExpressRouteCrossConnectionPeeringsOperations as OperationClass
    elif api_version == '2018-04-01':
        from .v2018_04_01.operations import ExpressRouteCrossConnectionPeeringsOperations as OperationClass
    else:
        raise NotImplementedError('APIVersion {} is not available'.format(
            api_version))
    return OperationClass(self._client, self.config, Serializer(self.
        _models_dict(api_version)), Deserializer(self._models_dict(
        api_version)))