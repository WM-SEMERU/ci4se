def invite_users(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.invite_users_with_http_info(**kwargs)
    else:
        data = self.invite_users_with_http_info(**kwargs)
        return data