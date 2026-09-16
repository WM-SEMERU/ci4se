def GetService(self, service_name, version=sorted(_SERVICE_MAP.keys())[-1],
    server=None):
    if not server:
        server = DEFAULT_ENDPOINT
    server = server[:-1] if server[-1] == '/' else server
    try:
        service = googleads.common.GetServiceClassForLibrary(self.soap_impl)(
            self._SOAP_SERVICE_FORMAT % (server, version, service_name),
            self._header_handler, _AdManagerPacker, self.proxy_config, self
            .timeout, version, cache=self.cache)
        return service
    except googleads.errors.GoogleAdsSoapTransportError:
        if version in _SERVICE_MAP:
            if service_name in _SERVICE_MAP[version]:
                raise
            else:
                raise googleads.errors.GoogleAdsValueError(
                    'Unrecognized service for the Ad Manager API. Service given: %s Supported services: %s'
                     % (service_name, _SERVICE_MAP[version]))
        else:
            raise googleads.errors.GoogleAdsValueError(
                'Unrecognized version of the Ad Manager API. Version given: %s Supported versions: %s'
                 % (version, _SERVICE_MAP.keys()))