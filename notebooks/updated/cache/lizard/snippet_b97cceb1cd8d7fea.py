def delete_storage_class(self, name, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.delete_storage_class_with_http_info(name, **kwargs)
    else:
        data = self.delete_storage_class_with_http_info(name, **kwargs)
        return data