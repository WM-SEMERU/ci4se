def _unregister_service(self):
    if self._registration is not None:
        try:
            self._registration.unregister()
        except BundleException as ex:
            logger = logging.getLogger('-'.join((self._ipopo_instance.name,
                'ServiceRegistration')))
            logger.error('Error unregistering a service: %s', ex)
        self._ipopo_instance.safe_callback(ipopo_constants.
            IPOPO_CALLBACK_POST_UNREGISTRATION, self._svc_reference)
        self._registration = None
        self._svc_reference = None