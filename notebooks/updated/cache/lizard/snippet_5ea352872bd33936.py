def group_create(self, group, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.group_create_with_http_info(group, **kwargs)
    else:
        data = self.group_create_with_http_info(group, **kwargs)
        return data