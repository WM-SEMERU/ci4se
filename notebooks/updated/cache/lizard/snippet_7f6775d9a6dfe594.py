def clear(self):
    with self.__svc_lock:
        self.__svc_registry.clear()
        self.__svc_factories.clear()
        self.__svc_specs.clear()
        self.__bundle_svc.clear()
        self.__bundle_imports.clear()
        self.__factory_usage.clear()
        self.__pending_services.clear()