def firmware_manifest_destroy(self, manifest_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.firmware_manifest_destroy_with_http_info(manifest_id,
            **kwargs)
    else:
        data = self.firmware_manifest_destroy_with_http_info(manifest_id,
            **kwargs)
        return data