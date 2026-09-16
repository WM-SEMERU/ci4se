def set_connection(self, service_name, to_cache):
    self.services.setdefault(service_name, {})
    self.services[service_name]['connection'] = to_cache