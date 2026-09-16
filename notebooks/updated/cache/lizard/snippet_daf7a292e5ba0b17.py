def get_user(self, user_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return self.get_user_with_http_info(user_id, **kwargs)
    else:
        data = self.get_user_with_http_info(user_id, **kwargs)
        return data