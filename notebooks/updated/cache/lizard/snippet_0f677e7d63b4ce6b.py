def iter_services(self, service_group=None):
    if service_group is not None:
        if service_group not in EFConfig.SERVICE_GROUPS:
            raise RuntimeError(
                "service registry: {} doesn't have '{}' section listed in EFConfig"
                .format(self._service_registry_file, service_group))
        return self.service_registry_json[service_group].iteritems()
    else:
        return self.services().iteritems()