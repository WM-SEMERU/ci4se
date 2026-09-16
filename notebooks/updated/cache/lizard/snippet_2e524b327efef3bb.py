def execute_or_create_resource(self, device_id, _resource_path, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.execute_or_create_resource_with_http_info(device_id,
            _resource_path, **kwargs)
    else:
        data = self.execute_or_create_resource_with_http_info(device_id,
            _resource_path, **kwargs)
        return data