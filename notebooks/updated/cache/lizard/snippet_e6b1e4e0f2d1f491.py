def cancel_all_builds_in_group(self, id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('callback'):
        return self.cancel_all_builds_in_group_with_http_info(id, **kwargs)
    else:
        data = self.cancel_all_builds_in_group_with_http_info(id, **kwargs)
        return data