def GenApiConfig(service_class_names, config_string_generator=None,
    hostname=None, application_path=None, **additional_kwargs):
    api_service_map = collections.OrderedDict()
    resolved_services = []
    for service_class_name in service_class_names:
        module_name, base_service_class_name = service_class_name.rsplit('.', 1
            )
        module = __import__(module_name, fromlist=base_service_class_name)
        service = getattr(module, base_service_class_name)
        if hasattr(service, 'get_api_classes'):
            resolved_services.extend(service.get_api_classes())
        elif not isinstance(service, type) or not issubclass(service,
            remote.Service):
            raise TypeError('%s is not a ProtoRPC service' % service_class_name
                )
        else:
            resolved_services.append(service)
    for resolved_service in resolved_services:
        services = api_service_map.setdefault((resolved_service.api_info.
            name, resolved_service.api_info.api_version), [])
        services.append(resolved_service)
    app_yaml_hostname = _GetAppYamlHostname(application_path)
    service_map = collections.OrderedDict()
    config_string_generator = (config_string_generator or api_config.
        ApiConfigGenerator())
    for api_info, services in api_service_map.iteritems():
        assert services, 'An API must have at least one ProtoRPC service'
        hostname = services[0
            ].api_info.hostname or hostname or app_yaml_hostname
        service_map['%s-%s' % api_info
            ] = config_string_generator.pretty_print_config_to_json(services,
            hostname=hostname, **additional_kwargs)
    return service_map