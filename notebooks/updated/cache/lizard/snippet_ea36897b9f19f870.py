def get_account_info(self, account_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_account_info_with_http_info(account_id, **kwargs)
    else:
        data = self.get_account_info_with_http_info(account_id, **kwargs)
        return data