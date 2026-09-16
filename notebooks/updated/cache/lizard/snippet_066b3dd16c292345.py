def add_service_spec(self, service_spec):
    assert service_spec is not None
    if service_spec.name in self.service_specs:
        raise ThriftCompilerError(
            'Cannot define service "%s". That name is already taken.' %
            service_spec.name)
    self.service_specs[service_spec.name] = service_spec