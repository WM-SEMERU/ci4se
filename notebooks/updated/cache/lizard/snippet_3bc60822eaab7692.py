def service_headline(self, short_name):
    if short_name not in self.services:
        raise ArgumentError('Unknown service name', short_name=short_name)
    return self.services[short_name]['state'].headline