def get_pre_subscriptions(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_pre_subscriptions_with_http_info(**kwargs)
    else:
        data = self.get_pre_subscriptions_with_http_info(**kwargs)
        return data