def get_customer_preferences(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.get_customer_preferences_with_http_info(**kwargs)
    else:
        data = self.get_customer_preferences_with_http_info(**kwargs)
        return data