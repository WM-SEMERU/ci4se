def get_users_of_group(self, group_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_users_of_group_with_http_info(group_id, **kwargs)
    else:
        data = self.get_users_of_group_with_http_info(group_id, **kwargs)
        return data