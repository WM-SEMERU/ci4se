def client_for(service, service_module, thrift_service_name=None):
    assert service_module, 'service_module is required'
    service = service or ''
    if not thrift_service_name:
        thrift_service_name = service_module.__name__.rsplit('.', 1)[-1]
    method_names = get_service_methods(service_module.Iface)

    def init(self, tchannel, hostport=None, trace=False, protocol_headers=None
        ):
        self.async_thrift = self.__async_client_class__(tchannel=tchannel,
            hostport=hostport, trace=trace, protocol_headers=protocol_headers)
        self.threadloop = tchannel._threadloop
    init.__name__ = '__init__'
    methods = {'__init__': init, '__async_client_class__': async_client_for
        (service=service, service_module=service_module,
        thrift_service_name=thrift_service_name)}
    methods.update({method_name: generate_method(method_name) for
        method_name in method_names})
    return type(thrift_service_name + 'Client', (object,), methods)