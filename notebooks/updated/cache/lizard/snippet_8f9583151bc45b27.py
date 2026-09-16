def _parse_method_data(self, method_name, method_data):
    method_params = {}
    method_models = {}
    if 'parameters' in method_data:
        for param in method_data['parameters']:
            p = _Swagger.SwaggerParameter(param)
            if p.name:
                method_params[p.name] = True
            if p.schema:
                method_models['application/json'] = p.schema
    request_templates = (_Swagger.REQUEST_OPTION_TEMPLATE if method_name ==
        'options' else _Swagger.REQUEST_TEMPLATE)
    integration_type = 'MOCK' if method_name == 'options' else 'AWS'
    return {'params': method_params, 'models': method_models,
        'request_templates': request_templates, 'integration_type':
        integration_type}