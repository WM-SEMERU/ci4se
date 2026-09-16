def matches(self, *specs):
    for spec in specs:
        if ':' in spec:
            app_name, endpoint_name = spec.split(':')
        else:
            app_name, endpoint_name = spec, None
        for endpoint in self.endpoints:
            if app_name == endpoint.application.name and endpoint_name in (
                endpoint.name, None):
                break
        else:
            return False
    return True