def update_my_account(self, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.update_my_account_with_http_info(body, **kwargs)
    else:
        data = self.update_my_account_with_http_info(body, **kwargs)
        return data