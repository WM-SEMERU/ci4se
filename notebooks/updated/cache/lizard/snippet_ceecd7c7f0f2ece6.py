def revoke_number(self, number, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return self.revoke_number_with_http_info(number, **kwargs)
    else:
        data = self.revoke_number_with_http_info(number, **kwargs)
        return data