def get_users_of_account_group(self, account_id, group_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_users_of_account_group_with_http_info(account_id,
            group_id, **kwargs)
    else:
        data = self.get_users_of_account_group_with_http_info(account_id,
            group_id, **kwargs)
        return data