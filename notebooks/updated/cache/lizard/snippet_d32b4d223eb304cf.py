def _configure_manager(self):
    self._flavor_manager = CloudCDNFlavorManager(self, uri_base='flavors',
        resource_class=CloudCDNFlavor, response_key=None,
        plural_response_key='flavors')
    self._services_manager = CloudCDNServiceManager(self, uri_base=
        'services', resource_class=CloudCDNService, response_key=None,
        plural_response_key='services')