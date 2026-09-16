def group_update(self, device_group_id, group, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.group_update_with_http_info(device_group_id, group, **
            kwargs)
    else:
        data = self.group_update_with_http_info(device_group_id, group, **
            kwargs)
        return data