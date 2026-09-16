def _stop(self):
    self.__context.remove_service_listener(self)
    try:
        with use_ipopo(self.__context) as ipopo:
            ipopo.remove_listener(self)
    except BundleException:
        pass