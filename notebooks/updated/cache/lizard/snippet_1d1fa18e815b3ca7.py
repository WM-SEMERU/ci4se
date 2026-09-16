def firmware_manifest_list(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.firmware_manifest_list_with_http_info(**kwargs)
    else:
        data = self.firmware_manifest_list_with_http_info(**kwargs)
        return data