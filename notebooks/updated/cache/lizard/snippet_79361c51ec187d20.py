def read_custom_resource_definition_status(self, name, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.read_custom_resource_definition_status_with_http_info(name,
            **kwargs)
    else:
        data = self.read_custom_resource_definition_status_with_http_info(name,
            **kwargs)
        return data