def vpn_sites_configuration(self):
    api_version = self._get_api_version('vpn_sites_configuration')
    if api_version == '2018-04-01':
        from .v2018_04_01.operations import VpnSitesConfigurationOperations as OperationClass
    else:
        raise NotImplementedError('APIVersion {} is not available'.format(
            api_version))
    return OperationClass(self._client, self.config, Serializer(self.
        _models_dict(api_version)), Deserializer(self._models_dict(
        api_version)))