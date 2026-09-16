def replace_csi_driver(self, name, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.replace_csi_driver_with_http_info(name, body, **kwargs)
    else:
        data = self.replace_csi_driver_with_http_info(name, body, **kwargs)
        return data