def model_resource(self, resource_name):
    resource = first([resource for resource in self.api._registry.values() if
        resource.get_api_name() == resource_name])
    data = {'apiVersion': '0.1', 'swaggerVersion': '1.1', 'basePath': 
        '%s%s' % (self.base_uri(), self.api.url_prefix), 'resourcePath': 
        '/meta/%s' % resource.get_api_name(), 'apis': self.get_model_apis(
        resource), 'models': self.get_model(resource)}
    response = jsonify(data)
    response.headers.add('Cache-Control', 'max-age=0')
    return response